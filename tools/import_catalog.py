#!/usr/bin/env python3
"""One-off import: turn a directory of per-repo catalog JSON files into data/apps.json.

Usage:
    python3 tools/import_catalog.py CATALOG_DIR --exclude-file RULES.txt [--fresh]

The exclude file is a LOCAL text file that is never committed (its name is in .gitignore). One rule
per line, '#' starts a comment:
    name: REPO_NAME            exclude this repository (case-insensitive); also removed from text
    prefix: abc_               exclude repository names starting with this
    contains: xyz            exclude repository names containing this
    note: some phrase          exclude records whose notes contain this phrase
    private-kind: data         exclude private repositories of this kind
    word: oldword=newword    replace an ordinary word in text

Default is a merge: records already in data/apps.json are kept as they are (so hand corrections
survive), excluded ones are dropped, catalog records that are not in apps.json yet are added.
--fresh rebuilds apps.json from the catalog only. Writes data/apps.json and data/meta.json.
Standard library only.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import build_map as bm  # noqa: E402

TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*[A-Za-z0-9]|[A-Za-z0-9]")


class Rules:
    def __init__(self, path):
        self.names, self.prefixes, self.contains, self.notes, self.kinds, self.words = set(), [], [], [], [], {}
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                key, _, val = line.partition(":")
                val = val.strip()
                key = key.strip().lower()
                if key == "name":
                    self.names.add(val.lower())
                elif key == "prefix":
                    self.prefixes.append(val.lower())
                elif key == "contains":
                    self.contains.append(val.lower())
                elif key == "note":
                    self.notes.append(val.lower())
                elif key == "private-kind":
                    self.kinds.append(val.lower())
                elif key == "word":
                    a, _, b = val.partition("=")
                    self.words[a.strip()] = b.strip()
                else:
                    sys.exit("unknown rule: " + line)

    def reason(self, rec):
        n = rec.get("repo", "").lower()
        if n in self.names or n.startswith(tuple(self.prefixes)) or any(c in n for c in self.contains):
            return "name rule or personal/client/third-party list"
        if any(x in (rec.get("notes") or "").lower() for x in self.notes):
            return "catalog note says excluded"
        if rec.get("visibility") == "private" and rec.get("kind") in self.kinds:
            return "private data archive"
        return None

    def scrub_text(self, s):
        def tok(m):
            t = m.group(0)
            if re.fullmatch(r"[a-z]+", t):
                return t
            return "a private repo" if t.lower() in self.names else t
        for a, b in self.words.items():
            s = re.sub(r"\b%s\b" % re.escape(a), b, s)
        return TOKEN_RE.sub(tok, s)

    def scrub(self, v):
        if isinstance(v, str):
            return self.scrub_text(v)
        if isinstance(v, list):
            out = []
            for x in v:
                if isinstance(x, str):
                    head = TOKEN_RE.findall(x)
                    if head and head[0].lower() in self.names:
                        continue
                out.append(self.scrub(x))
            return out
        if isinstance(v, dict):
            return {k: self.scrub(x) for k, x in v.items()}
        return v


def atomic_write(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, path)


def main():
    args = sys.argv[1:]
    fresh = "--fresh" in args
    if "--exclude-file" not in args:
        sys.exit(__doc__)
    rules = Rules(args[args.index("--exclude-file") + 1])
    rest = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--exclude-file")]
    if len(rest) != 1:
        sys.exit(__doc__)
    files = sorted(glob.glob(os.path.join(rest[0], "*.json")))
    if not files:
        sys.exit("no *.json files in " + rest[0])
    path = os.path.join(bm.DATA, "apps.json")
    existing = {}
    if os.path.exists(path) and not fresh:
        with open(path, encoding="utf-8") as fh:
            existing = {r["repo"]: r for r in json.load(fh)}
    kept, excluded, log = {}, [], []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            rec = json.load(fh)
        why = rules.reason(rec)
        if why:
            excluded.append(why)
            continue
        kept[rec["repo"]] = existing.get(rec["repo"]) or bm.normalise_record(rec, log)
    for repo, rec in existing.items():
        if repo not in kept and not rules.reason(rec):
            kept[repo] = rec
    out = [rules.scrub(r) for r in kept.values()]
    out.sort(key=lambda r: r["repo"].lower())
    atomic_write(path, out)
    atomic_write(os.path.join(bm.DATA, "meta.json"), {"records_in": len(files), "excluded": len(excluded)})
    from collections import Counter
    print("records in:", len(files), "excluded:", len(excluded), "kept:", len(out))
    for k, v in sorted(Counter(excluded).items()):
        print("  excluded by", k, v)


if __name__ == "__main__":
    main()
