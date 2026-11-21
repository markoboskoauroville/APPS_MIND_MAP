#!/usr/bin/env python3
"""Build every generated file of APPS_MIND_MAP from data/apps.json (+ planned.json, guides.json).

    python3 tools/build_map.py            rewrite all generated files
    python3 tools/build_map.py --check    exit 1 if any generated file differs from disk (for CI)

Standard library only. Output is deterministic: running it twice changes nothing.
Generated: README.md MIND_MAP.md CAPABILITIES.md (+ capabilities/*.md when large) KEYWORDS.md
CONTROL_API.md HARDWARE.md MODULES.md CONNECTIONS.md STATUS.md index.html apps/*.md.
Edit data/*.json, never the outputs. The privacy filter is not here: data/apps.json is already
filtered by tools/import_catalog.py.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.dont_write_bytecode = True

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OWNER = "markoboskoauroville"
GH = "https://github.com/" + OWNER + "/"
MAX_ONE_LINE = 160

# ---------------------------------------------------------------------------
# Vocabularies
# ---------------------------------------------------------------------------
CATS = [
    ("voice-dictation-transcription", "Voice, dictation and transcription"),
    ("audio-music-dj", "Audio, music and DJ"),
    ("mixer-midi-audio-hardware", "Mixers, MIDI and audio hardware"),
    ("camera-video-ndi-streaming", "Camera, video, NDI and streaming"),
    ("film-editing-resolve", "Film and editing (DaVinci Resolve)"),
    ("ai-agents-claude-tooling", "AI agents and Claude tooling"),
    ("mac-system-utilities", "Mac system utilities"),
    ("android-termux", "Android and Termux"),
    ("remote-control-networking", "Remote control and networking"),
    ("lights-keyboard-visuals", "Lights, keyboard and visuals"),
    ("wellbeing-sound-meditation", "Wellbeing, sound and meditation"),
    ("websites-pages", "Websites and pages"),
    ("knowledge-books-guides", "Knowledge, books and guides"),
    ("learning-academy", "Learning and academy"),
    ("maps-travel-location", "Maps, travel and location"),
    ("keys-secrets-infrastructure", "Keys, secrets and infrastructure"),
    ("data-backups-misc", "Data, backups and misc"),
]
CAT_TITLE = dict(CATS)
PLATFORMS = ["macOS", "Android", "Termux", "Windows", "Linux", "Web", "Cloud", "iOS", "Hammerspoon", "Chrome"]
PLATFORM_ALIAS = {"mac": "macOS", "macos": "macOS", "osx": "macOS", "os x": "macOS", "android": "Android",
                  "termux": "Termux", "windows": "Windows", "win": "Windows", "linux": "Linux", "web": "Web",
                  "browser": "Web", "cloud": "Cloud", "ios": "iOS", "iphone": "iOS", "hammerspoon": "Hammerspoon",
                  "chrome": "Chrome", "chromium": "Chrome"}
KINDS = ["app", "cli-tool", "library-module", "service-daemon", "browser-extension", "website",
         "content-book-guide", "data", "config", "fork", "experiment", "empty"]
STATUSES = ["active", "dormant", "archived", "empty"]
LEVELS = ["door", "http", "other", "cli", "adb", "accessibility", "none"]
LEVEL_TITLE = {
    "door": "Standard door (/health, /api, POST /api/<action>)",
    "http": "Own HTTP routes",
    "other": "Other protocols (OSC, MIDI, WebSocket, URL scheme)",
    "cli": "Command line or script only",
    "adb": "Android adb / intents",
    "accessibility": "Accessibility button ids only",
    "none": "No control API found",
}
KNOWN_KEYS = ["repo", "name", "aliases", "visibility", "kind", "category", "platforms", "language", "status",
              "last_push", "one_line", "does", "tasks", "control", "inputs", "outputs", "hardware", "depends_on",
              "talks_to", "reusable_modules", "build", "docs", "unmerged_branches", "confidence", "notes"]
KNOWN_CONTROL = ["has_api", "type", "port", "actions", "how_to_call", "evidence", "level"]

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
IPV4_RE = re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])")
PHONE_RE = re.compile(r"(?<![\w.:/-])(?:\+\d[\d ()-]{7,}\d|\d{3}[ -]\d{3}[ -]\d{4}|\d{10,})(?![\w-])")


def scrub(s):
    """Remove e-mail, foreign IPv4, phone numbers and home-directory user names from a string."""
    if not isinstance(s, str):
        return s
    s = re.sub(r"/Users/[A-Za-z0-9._-]+/", "~/", s)
    s = EMAIL_RE.sub("(address removed)", s)
    s = IPV4_RE.sub(lambda m: m.group(0) if m.group(0) in ("127.0.0.1", "0.0.0.0") else "(ip removed)", s)
    return PHONE_RE.sub("(number removed)", s)


def derive_level(c, notes=""):
    """control.level from type, actions, notes and has_api. Never upgrades beyond the evidence."""
    t = set(c.get("type") or [])
    acts = c.get("actions") or []
    if c.get("has_api") != "yes" and not acts:
        return "none"
    a = " ".join(acts).lower()
    has_health = "/health" in a
    has_api_route = bool(re.search(r"(?<![\w/])(?:get\s+)?/api(?![\w])", a))
    has_post = bool(re.search(r"post\s+/api/\S", a))
    door = has_health and has_api_route and ("remote-door-http" in t or has_post)
    if door and re.search(r"not (?:a|the) remote-door|no remote-door", notes or "", re.I):
        door = False
    if door:
        return "door"
    if "http" in t:
        return "http"
    if t & {"osc", "midi", "websocket", "url-scheme"}:
        return "other"
    if t & {"cli", "python-module"}:
        return "cli"
    if "adb-intent" in t:
        return "adb"
    if "accessibility" in t:
        return "accessibility"
    return "none"


def clean_list(v):
    out, seen = [], set()
    for x in v or []:
        if isinstance(x, str):
            x = re.sub(r"\s+", " ", scrub(x)).strip()
        if x in ("", None) or (isinstance(x, str) and x.lower() in seen):
            continue
        seen.add(x.lower() if isinstance(x, str) else x)
        out.append(x)
    return out


def norm_text(s):
    return re.sub(r"\s+", " ", scrub(s)).strip() if isinstance(s, str) else s


def normalise_record(r, log=None):
    """Cleaned copy of a record with fixed vocabularies and control.level. Extra keys are kept."""
    log = [] if log is None else log
    o = {}
    o["repo"] = r["repo"].strip()
    o["name"] = norm_text(r.get("name") or r["repo"]) or r["repo"]
    o["aliases"] = [a for a in clean_list(r.get("aliases")) if a.lower() != o["repo"].lower()]
    vis = str(r.get("visibility", "")).lower()
    if vis not in ("public", "private"):
        log.append("visibility defaulted to private")
        vis = "private"
    o["visibility"] = vis
    kind = str(r.get("kind", "")).lower().strip()
    if kind not in KINDS:
        log.append("kind %r -> experiment" % kind)
        kind = "experiment"
    o["kind"] = kind
    cat = str(r.get("category", "")).lower().strip()
    if cat not in CAT_TITLE:
        log.append("category %r -> data-backups-misc" % cat)
        cat = "data-backups-misc"
    o["category"] = cat
    plats = []
    for p in r.get("platforms") or []:
        q = PLATFORM_ALIAS.get(str(p).lower().strip(), p)
        if q != p:
            log.append("platform %r -> %s" % (p, q))
        if q in PLATFORMS and q not in plats:
            plats.append(q)
        elif q not in PLATFORMS:
            log.append("platform %r dropped" % p)
    o["platforms"] = sorted(plats, key=PLATFORMS.index)
    o["language"] = norm_text(r.get("language") or "unknown")
    st = str(r.get("status", "")).lower().strip()
    if st not in STATUSES:
        log.append("status %r -> dormant" % st)
        st = "dormant"
    if kind == "empty" and st != "empty":
        st = "empty"
    o["status"] = st
    lp = str(r.get("last_push") or "")[:10]
    o["last_push"] = lp if re.fullmatch(r"\d{4}-\d{2}-\d{2}", lp) else "unknown"
    o["one_line"] = norm_text(r.get("one_line") or "")
    o["does"] = clean_list(r.get("does"))
    o["tasks"] = clean_list(r.get("tasks"))
    c = r.get("control") or {}
    port = c.get("port")
    if isinstance(port, int):
        port = str(port)
    ctl = {k: v for k, v in c.items() if k not in KNOWN_CONTROL}
    ctl.update({
        "has_api": c.get("has_api") if c.get("has_api") in ("yes", "no", "unknown") else "unknown",
        "type": [t for t in (c.get("type") or []) if t],
        "port": norm_text(port) if port else None,
        "actions": clean_list(c.get("actions")),
        "how_to_call": norm_text(c.get("how_to_call")) or None,
        "evidence": norm_text(c.get("evidence") or "none found"),
    })
    ctl["level"] = c["level"] if c.get("level") in LEVELS else derive_level(ctl, r.get("notes") or "")
    o["control"] = ctl
    for k in ("inputs", "outputs", "hardware", "depends_on", "talks_to"):
        o[k] = clean_list(r.get(k))
    o["reusable_modules"] = [{"path": norm_text(m["path"]), "what": norm_text(m.get("what") or "")}
                             for m in (r.get("reusable_modules") or []) if isinstance(m, dict) and m.get("path")]
    b = r.get("build") or {}
    o["build"] = {"workflow": b.get("workflow") if b.get("workflow") in ("yes", "no") else "no",
                  "release": b.get("release") or None}
    o["docs"] = clean_list(r.get("docs"))
    o["unmerged_branches"] = int(r.get("unmerged_branches") or 0)
    conf = str(r.get("confidence", "")).lower()
    o["confidence"] = conf if conf in ("high", "medium", "low") else "low"
    o["notes"] = norm_text(r.get("notes") or "")
    for k, v in r.items():
        if k not in KNOWN_KEYS and k not in o:
            o[k] = v
    return o


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------
def _wrap_placeholders(part):
    def wrap(m):
        t, tail = m.group(1), ""
        while t and t[-1] in ".,;:)":
            tail = t[-1] + tail
            t = t[:-1]
        return "`" + t + "`" + tail
    return re.sub(r"(?<!\S)(\S*<[A-Za-z_][\w-]*>\S*)", wrap, part)


def esc(s):
    """Text for markdown: placeholders like /api/<action> become code spans, other angle brackets are replaced."""
    s = re.sub(r"\s+", " ", str(s)).strip()
    out = []
    for p in re.split(r"(`[^`]*`)", s):
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append(p)
        else:
            out.append(_wrap_placeholders(p))
    s = "".join(out)
    out = []
    for p in re.split(r"(`[^`]*`)", s):
        out.append(p if p.startswith("`") and p.endswith("`") and len(p) > 1 else p.replace("<", "‹").replace(">", "›"))
    return "".join(out)


def cell(s):
    return esc(s).replace("|", "\\|")


def cs(s, table=False):
    """Inline code span."""
    s = re.sub(r"\s+", " ", str(s)).strip()
    if table:
        s = s.replace("|", "\\|")
    if "`" in s:
        return "`` " + s + " ``"
    return "`" + s + "`"


def link_text(s):
    return esc(s).replace("[", "(").replace("]", ")")


def tidy(s):
    s = re.sub(r"\s+", " ", s or "").strip().rstrip(" ;,:")
    return s + "." if s and s[-1] not in ".!?" else s


def gh_anchor(h):
    h = h.strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def first_int(s):
    m = re.search(r"\b(\d{4,5})\b", s or "")
    return m.group(1) if m else None


def norm_key(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def short_name(rec):
    return re.sub(r"\s*\([^)]*\)", "", rec["name"]).strip() or rec["name"]


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.;])\s+", text or "") if s.strip()]


def load_json(name, default):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return default
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*[A-Za-z0-9]|[A-Za-z0-9]")

# ---------------------------------------------------------------------------
# Context: display names, retired flags, port collisions
# ---------------------------------------------------------------------------
CTX = {"collide": set(), "retired": {}, "ports": {}, "by": {}}

RETIRED_START = re.compile(r"^(?:do not use|retired|obsolete|merged|superseded|archived|description says archive|github marks it archived)", re.I)
RETIRED_ANY = re.compile(r"\b(?:retired \d|is retired|was retired|do not use|merged (?:on [\d.]+ )?into|(?:later )?superseded by|superseded in practice by|replaced by the|moved to)\b", re.I)


def retired_info(rec):
    """(is_retired, sentence naming the replacement or None)."""
    if rec.get("retired") in (True, "yes") or rec.get("replaced_by"):
        rb = rec.get("replaced_by")
        return True, (("Replaced by " + rb) if rb else None)
    notes = rec.get("notes") or ""
    sens = sentences(notes)
    first = sens[0] if sens else ""
    hit = None
    if rec["status"] == "archived":
        hit = first
    if RETIRED_START.match(first) and not re.match(r"superseded versions", first, re.I):
        hit = first
    else:
        for s in sens:
            if RETIRED_ANY.search(s) and not re.match(r"replaces", s, re.I) and re.search(r"\b(?:this|it|repo)\b|^[A-Z]", s) and rec["status"] != "active":
                hit = s
                break
    if hit is None and rec["status"] != "archived":
        return False, None
    return True, hit


def setup_context(cards, planned):
    CTX["by"] = {r["repo"]: r for r in cards}
    names = Counter(norm_key(r["name"]) for r in cards)
    for p in planned:
        names[norm_key(p["name"])] += 1
    CTX["collide"] = {k for k, v in names.items() if v > 1}
    resolve = build_resolver(cards)
    CTX["resolve"] = resolve
    for r in cards:
        flag, sent = retired_info(r)
        rep = None
        if flag:
            rb = r.get("replaced_by")
            cand = []
            if rb:
                cand.append(rb)
            elif sent:
                cand += re.findall(r"(?:use|by|into|to|the repo)\s+(?:the repo\s+)?([A-Za-z][\w-]*(?: [A-Z][\w-]*)*)", sent)
            for c in cand:
                for t in [c] + c.split(" ")[:1] + c.split("/")[:1]:
                    x = resolve(t)
                    if x and x != r["repo"]:
                        rep = x
                        break
                if rep:
                    break
        CTX["retired"][r["repo"]] = (flag, rep, sent)
    ports = defaultdict(list)
    for r in cards:
        p = first_int(r["control"]["port"])
        if p and r["control"]["level"] != "none":
            ports[p].append(r["repo"])
    CTX["ports"] = {p: v for p, v in ports.items() if len(v) > 1}


def is_retired(rec):
    return CTX["retired"].get(rec["repo"], (False,))[0]


def dname(rec, md=True):
    """Display name: unique across the map; collisions get the repo name; retired gets a marker."""
    n = link_text(rec["name"]) if md else rec["name"]
    if norm_key(rec["name"]) in CTX["collide"]:
        n += (" `%s`" % rec["repo"]) if md else " (%s)" % rec["repo"]
    if rec.get("_planned"):
        n += " (planned)"
    elif is_retired(rec):
        n += " (retired)"
    return n


def plain_name(rec, limit=40):
    n = short_name(rec)
    if norm_key(rec["name"]) in CTX["collide"] or any(
            norm_key(short_name(o)) == norm_key(n) and o["repo"] != rec["repo"] for o in CTX["by"].values()):
        n += " " + rec["repo"]
    if rec.get("_planned"):
        n += " PLANNED"
    elif is_retired(rec):
        n += " RETIRED"
    return mm_label(n, limit)


def tag_label(rec):
    lv = rec["control"]["level"]
    if lv in ("door", "http"):
        p = first_int(rec["control"]["port"])
        return "%s %s" % (lv, p) if p else lv
    return lv


def card_link(rec, prefix="apps/"):
    return "[%s](%s%s.md)" % (dname(rec), prefix, rec["repo"])


def card_link_plain(rec, prefix="apps/"):
    n = rec["name"] + " (%s)" % rec["repo"]
    if rec.get("_planned"):
        n += " (planned)"
    elif is_retired(rec):
        rep = CTX["retired"][rec["repo"]][1]
        n += (" (retired, use %s)" % rep) if rep else " (retired)"
    return "[%s](%s%s.md)" % (link_text(n), prefix, rec["repo"])


def mm_label(s, limit=44):
    s = s.replace("&", " and ")
    s = re.sub(r"[^\w\s.+/-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > limit:
        s = s[:limit].rsplit(" ", 1)[0]
    return s or "app"


def mq_label(s, limit=90):
    """Label for a quoted edge text: keeps readable punctuation, drops what Mermaid reads as syntax."""
    s = s.replace("&", " and ")
    s = re.sub(r"[\"|\[\]{}<>`#%]", " ", s)
    return re.sub(r"\s+", " ", s).strip()[:limit].strip() or "link"


def render(path, text):
    return text if text.endswith("\n") else text + "\n"


# ---------------------------------------------------------------------------
# Name resolution (aliases -> repo)
# ---------------------------------------------------------------------------
def build_resolver(recs):
    keys = defaultdict(set)
    for r in recs:
        for s in [r["repo"], r["name"], short_name(r)] + r["aliases"]:
            k = norm_key(s)
            if len(k) >= 4:
                keys[k].add(r["repo"])
    amb = {k: next(iter(v)) for k, v in keys.items() if len(v) == 1}
    repos = {r["repo"].lower(): r["repo"] for r in recs}

    def resolve(text):
        t = re.sub(r"\s+", " ", text).strip()
        base = re.sub(r"\s*\(.*", "", t).strip()
        cands = [t, base]
        cands += [x.strip() for x in re.split(r"\s+[-/:,;]\s+|,|;| / | \+ ", base) if x.strip()][:1]
        head = TOKEN_RE.findall(base)
        if head:
            cands.append(head[0])
        for c in cands:
            if c.lower() in repos:
                return repos[c.lower()]
            k = norm_key(c)
            if k in amb:
                return amb[k]
        return None

    return resolve


def compute_edges(recs, resolve):
    edges = {}
    for r in recs:
        for kind, label in (("depends_on", "uses"), ("talks_to", "talks to")):
            for it in r[kind]:
                dst = resolve(it)
                if dst and dst != r["repo"]:
                    key = (r["repo"], dst)
                    if key not in edges or label == "uses":
                        edges[key] = label
    return sorted((a, b, l) for (a, b), l in edges.items())


# ---------------------------------------------------------------------------
# Planned apps (data/planned.json)
# ---------------------------------------------------------------------------
def planned_rec(p):
    """A record-shaped view of a planned app so the generators can treat it like the others."""
    return {
        "repo": p["repo"], "name": p["name"], "aliases": p.get("aliases", []), "visibility": "public",
        "kind": "app", "category": p["category"], "platforms": p.get("platforms", ["macOS"]), "language": "not written yet",
        "status": "planned", "last_push": "n/a", "one_line": p["one_line"], "does": p.get("does", []),
        "tasks": p.get("tasks", []), "hardware": p.get("hardware", []), "inputs": [], "outputs": [],
        "depends_on": [], "talks_to": [], "reusable_modules": [], "notes": p.get("notes", ""), "docs": [],
        "control": {"has_api": "no", "type": ["none"], "port": None, "actions": [], "how_to_call": None,
                    "evidence": "none found", "level": "none"},
        "build": {"workflow": "no", "release": None}, "unmerged_branches": 0, "confidence": "low",
        "_planned": True, "_prompt": p["prompt"], "_keywords": p.get("keywords", []), "_id": p.get("id", ""),
        "_edges": p.get("edges", []),
    }


def edge_arrow(d):
    return {"out": "->", "in": "<-", "both": "<->"}[d]


def planned_edge_target(e, by_repo):
    if e.get("to"):
        return by_repo[e["to"]]
    return None


def edge_text(e, by_repo, prefix="apps/"):
    tgt = card_link_plain(by_repo[e["to"]], prefix) if e.get("to") else esc(e["external"]) + " (not a repo on this map)"
    port = " [%s]" % e["port"] if e.get("port") else ""
    return "%s %s%s: %s" % (edge_arrow(e["dir"]), tgt, port, esc(e["label"]))


# ---------------------------------------------------------------------------
# Cards
# ---------------------------------------------------------------------------
def bullets(items):
    return "".join("- %s\n" % esc(i) for i in items)


def doc_item(rec, d):
    if rec["visibility"] == "public" and re.fullmatch(r"[\w./-]+", d):
        return "[%s](%sblob/HEAD/%s)" % (d, GH + rec["repo"] + "/", d)
    return cs(d)


def cat_target(slug, prefix=""):
    """Link target for a category: anchor in CAPABILITIES.md or a file in capabilities/."""
    if CTX.get("split"):
        return "%scapabilities/%s.md" % (prefix, slug)
    return "%sCAPABILITIES.md#%s" % (prefix, gh_anchor(CAT_TITLE[slug]))


def build_card(rec, by_repo, out_edges, in_edges, planned_links):
    c = rec["control"]
    flag, rep, sent = CTX["retired"][rec["repo"]]
    L = ["# %s%s" % (esc(rec["name"]), " (retired)" if flag else ""), "",
         "[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Control API](../CONTROL_API.md) | [Connections](../CONNECTIONS.md)",
         ""]
    if flag:
        L += ["> **Retired - do not use.** " + ("Replaced by %s. " % card_link(by_repo[rep], "") if rep else "") +
              (esc(tidy(sent)) if sent else ""), ""]
    if rec["one_line"]:
        L += ["**%s**" % esc(rec["one_line"]), ""]
    plats = ", ".join(rec["platforms"]) or "unknown"
    vis = rec["visibility"] + (" (code not readable without access)" if rec["visibility"] == "private" else "")
    rel = rec["build"]["release"] or "none recorded"
    facts = [
        ("Repo", "[%s/%s](%s%s)" % (OWNER, rec["repo"], GH, rec["repo"])),
        ("Visibility", vis),
        ("Kind", rec["kind"]),
        ("Category", "[%s](%s)" % (CAT_TITLE[rec["category"]], cat_target(rec["category"], "../"))),
        ("Platforms", plats),
        ("Language", cell(rec["language"])),
        ("Status", "retired" if flag else rec["status"]),
        ("Last push", rec["last_push"]),
        ("Build / release", "GitHub workflow: %s; latest release: %s" % (rec["build"]["workflow"], cell(rel))),
        ("Control level", "%s (%s)" % (c["level"], LEVEL_TITLE[c["level"]].split(" (")[0].lower())),
    ]
    if rec["aliases"]:
        facts.insert(1, ("Also called", cell(", ".join(rec["aliases"]))))
    L += ["| Fact | Value |", "|---|---|"] + ["| %s | %s |" % f for f in facts] + [""]
    if rec["does"]:
        L += ["## What it can do", "", bullets(rec["does"]).rstrip(), ""]
    if rec["tasks"]:
        L += ["## Ask for it when", "", bullets(rec["tasks"]).rstrip(), ""]
    L += ["## How to control it", ""]
    if c["level"] == "none":
        L += ["No control API found." + (" The catalog notes some code-level hooks only." if c["actions"] else ""), ""]
    else:
        L += ["- Level: **%s**" % c["level"], "- Type: %s" % (", ".join(c["type"]) or "unknown")]
        if c.get("protocol"):
            L.append("- Protocol: %s" % esc(c["protocol"]))
        if c["port"]:
            L.append("- Port: %s" % esc(c["port"]))
        L.append("")
    p = first_int(c["port"])
    if p in CTX["ports"] and c["level"] != "none":
        others = [CTX["by"][x] for x in CTX["ports"][p] if x != rec["repo"]]
        L += ["**Warning:** port %s is also quoted for %s - confirm with `mantra-ports scan`." % (
            p, ", ".join(card_link(o, "") for o in others)), ""]
    if c["actions"]:
        L += ["Actions:", ""] + ["- %s" % cs(a) for a in c["actions"]] + [""]
    if c.get("before"):
        L += ["**Before you call:** %s" % esc(c["before"]), ""]
    if c["how_to_call"]:
        L += ["Example:", "", "```", c["how_to_call"].replace("```", "'''"), "```", ""]
    if c.get("examples"):
        L += ["More calls:", ""] + ["- %s: %s" % (esc(x["for"]), cs(x["call"])) for x in c["examples"]] + [""]
    if c["level"] != "none" or c["evidence"] not in ("none found", ""):
        L += ["Evidence: %s" % esc(c["evidence"]), ""]
    if rec["inputs"] or rec["outputs"]:
        L += ["## Inputs / Outputs", ""]
        if rec["inputs"]:
            L += ["Inputs:", "", bullets(rec["inputs"]).rstrip(), ""]
        if rec["outputs"]:
            L += ["Outputs:", "", bullets(rec["outputs"]).rstrip(), ""]
    if rec["hardware"]:
        L += ["## Hardware", "", bullets(rec["hardware"]).rstrip(), ""]
    uses = [by_repo[b] for (a, b, l) in out_edges.get(rec["repo"], []) if l == "uses"]
    talks = [by_repo[b] for (a, b, l) in out_edges.get(rec["repo"], []) if l == "talks to"]
    used_by = [by_repo[a] for (a, b, l) in in_edges.get(rec["repo"], [])]
    ww = []
    if uses:
        ww.append("- Uses: " + ", ".join(card_link(x, "") for x in uses))
    if talks:
        ww.append("- Talks to: " + ", ".join(card_link(x, "") for x in talks))
    if used_by:
        ww.append("- Used by or talked to by: " + ", ".join(card_link(x, "") for x in used_by))
    for pl, e in planned_links:
        back = {"out": "in", "in": "out", "both": "both"}[e["dir"]]
        ww.append("- Planned, not built: [%s](%s) %s %s%s" % (
            link_text(pl["name"]), "LIGHT_CONTROL.md" if pl["repo"] == "LIGHT_CONTROL" else pl["repo"] + ".md",
            {"out": "will be driven by this app", "in": "will drive this app", "both": "and this app will drive each other"}[back],
            "(%s)" % esc(e["label"]), (" [%s]" % e["port"]) if e.get("port") else ""))
    if ww:
        L += ["## Works with", ""] + ww + [""]
    if rec["reusable_modules"]:
        L += ["## Code worth reusing", ""]
        for m in rec["reusable_modules"]:
            L.append("- %s: %s" % (cs(m["path"]), esc(m["what"])))
        L.append("")
    if rec["notes"] or rec["unmerged_branches"]:
        L += ["## Notes", ""]
        if rec["notes"]:
            L += [esc(rec["notes"]), ""]
        if rec["unmerged_branches"]:
            L += ["Unmerged branches with commits ahead of main: %d." % rec["unmerged_branches"], ""]
    if rec["docs"]:
        L += ["## Docs in the repo", "", "\n".join("- " + doc_item(rec, d) for d in rec["docs"]), ""]
    if rec["confidence"] == "low":
        L += ["_Low confidence: little was documented in this repository. Check the code before relying on this card._", ""]
    return "\n".join(L)


def build_planned_card(p, by_repo):
    L = ["# %s (planned)" % esc(p["name"]), "",
         "[Map](../README.md) | [Capabilities](../CAPABILITIES.md) | [Connections](../CONNECTIONS.md)", "",
         "> **PLANNED - not built yet.** There is no repository and no API. The kickoff prompt is [%s](../%s)." % (p["_prompt"], p["_prompt"]), "",
         "**%s**" % esc(p["one_line"]), "",
         "| Fact | Value |", "|---|---|",
         "| Status | planned |",
         "| App id | %s |" % cell(p["_id"]),
         "| Also called | %s |" % cell(", ".join(p["aliases"])),
         "| Category | [%s](%s) |" % (CAT_TITLE[p["category"]], cat_target(p["category"], "../")),
         "| Platforms | %s |" % ", ".join(p["platforms"]), ""]
    if p["does"]:
        L += ["## What it is meant to do", "", bullets(p["does"]).rstrip(), ""]
    if p["tasks"]:
        L += ["## Ask for it when", "", bullets(p["tasks"]).rstrip(), "", "Until it is built, no app does this: see the planned links below for what exists today.", ""]
    if p["hardware"]:
        L += ["## Hardware", "", bullets(p["hardware"]).rstrip(), ""]
    L += ["## Planned links", "", "Arrow: `->` this app calls the other, `<-` the other calls this app, `<->` both.", ""]
    L += ["- " + edge_text(e, by_repo, "") for e in p["_edges"]] + [""]
    if p["_keywords"]:
        L += ["Keywords: " + ", ".join(p["_keywords"]), ""]
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Guides and gaps (data/guides.json)
# ---------------------------------------------------------------------------
def app_hay(r):
    return " ".join([r["name"], r["repo"], " ".join(r["aliases"]), " ".join(r["tasks"]), " ".join(r["hardware"])]).lower()


def assign_guides(guides, live):
    """Map category slug -> guides. A guide goes to the category whose live apps match its keywords most."""
    res = defaultdict(list)
    for g in guides:
        kws = [k.lower() for k in g.get("applies_to", [])]
        best, score = None, 0
        for slug, _ in CATS:
            n = sum(1 for r in live if r["category"] == slug and any(k in app_hay(r) for k in kws))
            if n > score:
                best, score = slug, n
        if best:
            res[best].append(g)
    return res


def guide_md(g, by_repo, prefix="apps/", level="###"):
    L = ["%s Which one to pick: %s" % (level, esc(g["title"])), ""]
    if g.get("text"):
        L += [g["text"].strip(), ""]
    if g.get("picks"):
        L += ["| You want | Use | How |", "|---|---|---|"]
        for p in g["picks"]:
            r = by_repo.get(p["use"])
            use = card_link_plain(r, prefix) if r else cs(p["use"], True)
            L.append("| %s | %s | %s |" % (cell(p["for"]), use, cs(p["how"], True) if p.get("how") else ""))
        L.append("")
    return L


def gaps_md(gaps, planned, level="##"):
    L = ["%s Not built yet" % level, "",
         "Searches that end here mean no app on this map does the job yet.", ""]
    for g in gaps:
        L.append("- **%s** (%s): %s" % (esc(g["need"]), g["status"], esc(g.get("note", ""))))
    for p in planned:
        L.append("- **%s** (planned): %s [kickoff prompt](%s)" % (esc(p["name"]), esc(p["one_line"]), p["_prompt"]))
    L.append("")
    return L


# ---------------------------------------------------------------------------
# Capabilities
# ---------------------------------------------------------------------------
def tasks_or_does(r):
    return r["tasks"] or r["does"][:3] or ([r["one_line"]] if r["one_line"] else [])


def cap_lines(r, prefix):
    out = []
    plat = "/".join(r["platforms"]) or "unknown"
    for i, t in enumerate(tasks_or_does(r)):
        ln = "- %s -> %s (%s; API: %s)" % (esc(t), card_link(r, prefix), plat, tag_label(r))
        if i == 0 and r["control"]["how_to_call"]:
            ln += " - call: " + cs(r["control"]["how_to_call"])
        out.append(ln)
    return out


def retired_line(r, prefix):
    flag, rep, sent = CTX["retired"][r["repo"]]
    s = "- %s" % card_link(r, prefix)
    if rep:
        s += " - replaced by %s" % card_link(CTX["by"][rep], prefix)
    elif sent:
        s += " - " + esc(tidy(sent))
    return s


def plain_name_md(r):
    n = short_name(r)
    if sum(1 for o in CTX["by"].values() if norm_key(short_name(o)) == norm_key(n)) > 1:
        n += " (%s)" % r["repo"]
    return esc(n)


def cat_section(slug, live, retired, planned, guides, by_repo, prefix, level):
    title = CAT_TITLE[slug]
    L = ["%s %s" % (level, title), ""]
    h = level + "#"
    for g in guides.get(slug, []):
        L += guide_md(g, by_repo, prefix, h)
    for r in sorted([r for r in live if r["category"] == slug], key=lambda r: (r["name"].lower(), r["repo"])):
        L += cap_lines(r, prefix)
    for p in planned:
        if p["category"] == slug:
            L.append("- %s -> %s (PLANNED, not built; no API yet) - [kickoff prompt](%s%s)" % (
                esc(p["tasks"][0] if p["tasks"] else p["one_line"]), card_link(p, prefix), prefix.replace("apps/", ""), p["_prompt"]))
    ret = sorted([r for r in retired if r["category"] == slug], key=lambda r: (r["name"].lower(), r["repo"]))
    if ret:
        L += ["", "%s Retired - do not use" % h, ""] + [retired_line(r, prefix) for r in ret]
    L.append("")
    return L


CAP_INTRO = ("One line per capability: `task -> app (platforms; API: how it is driven) - call: example`. "
             "The first line of each app carries the port and a working example. API values: `door N` (standard door on port N), `http N`, `cli`, `adb`, `accessibility`, `other`, `none`. "
             "Retired apps are listed per category under \"Retired - do not use\", never as live lines. "
             "Search: `grep -ri <word> CAPABILITIES.md capabilities/ KEYWORDS.md`, or open `index.html`.")


def gen_capabilities(cards, live, retired, planned, guides, gaps, by_repo):
    gmap = assign_guides(guides, live)
    cats = [s for s, _ in CATS if any(r["category"] == s for r in cards) or any(p["category"] == s for p in planned)]

    def index_block():
        L = ["## Categories", ""]
        for s in cats:
            n = sum(1 for r in live if r["category"] == s)
            names = ", ".join(plain_name_md(r) for r in sorted([r for r in live if r["category"] == s], key=lambda r: (r["name"].lower(), r["repo"]))[:14])
            L.append("- [%s](%s): %d apps - %s%s" % (CAT_TITLE[s], cat_target(s), n, names, ", and more" if n > 14 else ""))
        return L + [""]

    CTX["split"] = False
    single = ["# Capabilities: which app does what", "", CAP_INTRO, ""] + index_block() + gaps_md(gaps, planned)
    for s in cats:
        single += cat_section(s, live, retired, planned, gmap, by_repo, "apps/", "##")
    text = "\n".join(single)
    if text.count("\n") <= 1400 and len(text) <= 90000:
        return {"CAPABILITIES.md": text}
    CTX["split"] = True
    files = {}
    gl = [("- %s -> [%s](%s)" % (esc(g["title"]), CAT_TITLE[s], cat_target(s))) for s in cats for g in gmap.get(s, [])]
    idx = ["# Capabilities: which app does what", "", CAP_INTRO, "",
           "This index is small on purpose: pick the category, open its file (one file has all task lines of that category, with the port and a working call on the first line of each app). "
           "Guides that say which app to pick are at the top of each category file.", ""] + index_block() + (["## Which one to pick: guides", ""] + gl + [""] if gl else []) + gaps_md(gaps, planned)
    for s in cats:
        files["capabilities/%s.md" % s] = "\n".join(
            ["[Back to the index](../CAPABILITIES.md)", ""] + cat_section(s, live, retired, planned, gmap, by_repo, "../apps/", "#"))
    files["CAPABILITIES.md"] = "\n".join(idx)
    return files


# ---------------------------------------------------------------------------
# Keywords
# ---------------------------------------------------------------------------
STOP = set("""the and for with from that this into over any all one use used uses using new not are can its has have via per out off
than then them they their was were will would should could may also only more most other such each both when where which
while what who how why you your our his her she him about after before between without within under again once here there
some many much very just like make makes made get gets set sets run runs running show shows send sends take takes give gives
need needs want wants add adds list lists read reads write writes first second third own same different still already
two three four five six seven eight nine ten etc above across actually always being does done during instead never next
really something until whether work works dev app apps file files name names time back find check test tests local script
scripts status state update updates build builds link links copy button buttons word words tool tools data page pages text
code repo user users phone phones mac macs android web accept after against allow allows along among another around away
because become before behind below beside best better beyond bring brings came come comes consider could every few
former given goes going gone good great however into itself keep keeps kept know known last later least less let lets
long look looks lot made maybe might must neither none nor often once only onto onward others otherwise out outside part
perhaps put quite rather said say says see seem seems several since small so soon still sure take taken tell than through
thus together too toward towards try tries turn turns upon usually various way ways well went whatever whenever whole whose
will yet yes click clicks type types thing things single simple plain full open opens close closes start starts stop stops
called calls call able part parts item items real based plus minus per via off on in is it of to at by as be do if or an a
mantra mantras key keys cloud live lives setting settings install installs hold holds step steps monitor monitors save aloud pause pauses stream streams folder folders window windows session sessions message messages record records recording command commands control controls
screen switch serve server servers menu play plays microphone download downloads""".split())

EXTRA_WHITELIST = set("""claude google github croatian english hindi sanskrit german whisper groq gemini tailscale cloudflare suno
speechify resolve davinci ableton spotify firefox chrome chromium termux hammerspoon shizuku adb ndi hls midi osc usb
bluetooth wifi ssh vnc http websocket sony camera speech transcribe light""".split())


def kw_words(s):
    return [w for w in re.findall(r"[a-z][a-z0-9+#]{2,}", s.lower()) if w not in STOP]


def action_tokens(a):
    a = re.sub(r"^(?:GET|POST|PUT|DELETE|ANY)\s+", "", a.strip(), flags=re.I)
    m = re.match(r"(/[^\s{?]*)", a)
    out = []
    if m:
        segs = [x for x in m.group(1).split("/") if x and x != "api" and not x.startswith("<")]
        for sg in segs:
            if re.fullmatch(r"[a-z][a-z0-9_-]{2,}", sg.lower()):
                out.append(sg.lower())
    else:
        w = re.findall(r"[A-Za-z][\w-]{2,}", a)
        out += [x.lower() for x in w[:2]]
    return out


def build_keywords(live, retired, planned, gaps):
    """keyword -> {'forms': set, 'apps': set(repo), 'gaps': [gap]}"""
    allrecs = live + retired + planned
    by = {r["repo"]: r for r in allrecs}
    strong = defaultdict(set)
    weak = defaultdict(set)
    hw_apps = defaultdict(set)
    for r in allrecs:
        repo = r["repo"]
        toks = [r["name"], repo.replace("_", " ").replace("-", " ")] + r["aliases"] + r["hardware"] + r["tasks"]
        toks += list(r.get("_keywords", []))
        for s in toks:
            for w in kw_words(s):
                strong[w].add(repo)
        for s in r["hardware"] + list(r.get("_keywords", [])):
            for w in kw_words(s):
                hw_apps[w].add(repo)
        for s in r["does"]:
            for w in kw_words(s):
                weak[w].add(repo)
        for s in [repo] + r["aliases"] + [r["name"]]:
            if re.search(r"[-_]", s) and " " not in s.strip() and len(s) > 4:
                strong[s.lower()].add(repo)
        for port in re.findall(r"\b\d{4,5}\b", r["control"]["port"] or ""):
            strong[port].add(repo)
        for a in r["control"]["actions"]:
            for t in action_tokens(a):
                strong[t].add(repo)
        for x in r["control"].get("examples") or []:
            for w in kw_words(x["for"]):
                weak[w].add(repo)
    gap_src = defaultdict(list)
    for g in gaps:
        for w in kw_words(g["need"] + " " + " ".join(g.get("keywords", []))):
            gap_src[w].append(g)
    vocab = set(strong) | set(weak) | set(gap_src)
    canon = {}
    for w in vocab:
        if w.endswith("s") and not w.endswith("ss") and len(w) > 4 and w[:-1] in vocab:
            canon[w] = w[:-1]
    ent = {}
    for w in vocab:
        c = canon.get(w, w)
        e = ent.setdefault(c, {"forms": set(), "strong": set(), "weak": set(), "gaps": []})
        e["forms"].add(w)
        e["strong"] |= strong.get(w, set())
        e["weak"] |= weak.get(w, set())
        for g in gap_src.get(w, []):
            if g not in e["gaps"]:
                e["gaps"].append(g)
    white = {w for w, v in hw_apps.items() if len(v) <= 60} | EXTRA_WHITELIST
    out = {}
    for c, e in ent.items():
        e["apps"] = e["strong"] | e["weak"]
        if len(c) < 3 and not c.isdigit():
            continue
        if c in STOP:
            continue
        if len(e["apps"]) > 25 and not (e["forms"] & white):
            continue
        if not e["strong"] and len(e["weak"]) < 2 and not e["gaps"]:
            continue
        if not e["apps"] and not e["gaps"]:
            continue
        out[c] = e
    return out, by


def gen_keywords(live, retired, planned, gaps):
    ent, by = build_keywords(live, retired, planned, gaps)

    def order(repo):
        r = by[repo]
        return (1 if r.get("_planned") else 0, 1 if is_retired(r) else 0, r["name"].lower(), repo)

    L = ["# Keyword index", "",
         "Alphabetical. Each keyword lists every app that mentions it in its name, aliases, hardware, tasks, capabilities, port or action names; live apps first, then planned, then retired. "
         "Singular and plural are one entry (`light, lights`). Words that match more than 25 apps are left out unless they name hardware, a product or a protocol. "
         "Search with `grep -i <word> KEYWORDS.md`. An entry that says NOT BUILT YET means no app does it.", ""]
    cur = ""
    for w in sorted(ent):
        e = ent[w]
        head = w[0].upper() if w[0].isalpha() else "0-9"
        if head != cur:
            cur = head
            L += ["", "### " + head, ""]
        forms = sorted(e["forms"], key=lambda f: (len(f), f))
        items = [card_link_plain(by[x]) for x in sorted(e["apps"], key=lambda x: (1 if by[x].get("_planned") else 0, 1 if is_retired(by[x]) else 0, by[x]["name"].lower(), x))]
        line = "- **%s**: %s" % (", ".join(forms), ", ".join(items))
        for g in e["gaps"]:
            line += (" | " if items else "") + "NOT BUILT YET (%s): %s" % (g["status"], esc(g["need"]))
        L.append(line)
    return "\n".join(L), ent


# ---------------------------------------------------------------------------
# Control API
# ---------------------------------------------------------------------------
def gen_control(cards, live):
    L = ["# Control API: how to drive each app", "",
         "Apps are grouped by control level, derived from the catalog `type`, `actions` and `notes` and never upgraded beyond the evidence:", ""]
    for lv in LEVELS[:-1]:
        L.append("- **%s**: %s" % (lv, LEVEL_TITLE[lv]))
    L += ["", "The standard door: listen on `127.0.0.1` at a `MANTRA_PORTS` port; `GET /health`; `GET /api` (actions with a `does` sentence each); `POST /api/<action>` with a JSON body; answers `{ok, result}` or `{ok: false, error}`. From Python: `mantra_remote.call(\"<app-id>\", \"<action>\", **args)` through the Mantra Door, which launches a stopped app first. "
          "Never put a token, address or password in a call you write down; the Mantra Door token lives in a local file. Retired apps are marked (retired).", ""]
    for lv in LEVELS[:-1]:
        rs = sorted([r for r in cards if r["control"]["level"] == lv], key=lambda r: (is_retired(r), r["name"].lower(), r["repo"]))
        if not rs:
            continue
        L += ["## %s (%d)" % (LEVEL_TITLE[lv], len(rs)), "",
              "| App | Platform | Type | Port | Actions | How to call | Evidence |", "|---|---|---|---|---|---|---|"]
        for r in rs:
            c = r["control"]
            acts = c["actions"]
            shown = ", ".join(cs(a, True) for a in acts[:8])
            if len(acts) > 8:
                shown += " (+%d more, see card)" % (len(acts) - 8)
            L.append("| %s | %s | %s | %s | %s | %s | %s |" % (
                card_link(r), cell("/".join(r["platforms"])), cell(", ".join(c["type"])), cell(c["port"] or ""),
                shown, cs(c["how_to_call"], True) if c["how_to_call"] else "", cell(c["evidence"])))
        L.append("")
    todo = sorted([r for r in live if r["kind"] == "app" and r["control"]["level"] == "none"], key=lambda r: (r["name"].lower(), r["repo"]))
    L += ["## Apps without a door yet (%d)" % len(todo), "",
          "Kind `app` with no control API found, not retired. The rule is that every app ships the API, so this is the backlog.", ""]
    for slug, title in CATS:
        rs = [r for r in todo if r["category"] == slug]
        if rs:
            L += ["**%s**" % title, ""] + ["- %s (%s)" % (card_link(r), "/".join(r["platforms"]) or "unknown") for r in rs] + [""]
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Hardware
# ---------------------------------------------------------------------------
HW_FAMILIES = [
    ("Neewer Bluetooth LED light", r"neewer|led light|bluetooth led"),
    ("Sony cameras (Alpha, ILCE-7M5, A6600)", r"sony|alpha|ilce|a6600"),
    ("Allen & Heath CQ mixers", r"allen|cq-|\bcq\b"),
    ("Behringer XR18", r"behringer|xr18"),
    ("Ableton Live", r"ableton"),
    ("OXI E16 and MIDI controllers", r"oxi|midi|launchkey|hercules|\biac\b"),
    ("Logitech G815 keyboard and RGB lighting", r"g815|openrgb"),
    ("Elgato Stream Deck", r"stream deck"),
    ("Capture cards, webcams and NDI gear", r"cineview|accsoon|capture|webcam|mac cameras|\bndi\b"),
    ("Microphones, speakers and audio outputs", r"microphone|speaker|audio|blackhole|coreaudio|adam|xlr|hearing"),
    ("Android phones (Pixel, Nothing) and emulators", r"phone|pixel|nothing|android|termux|adb|hotspot|fingerprint|mpa"),
    ("Routers, cables and network adapters", r"router|ethernet|dongle|tp-link|\blan\b|thunderbolt|usb|tailscale|network"),
    ("Cloud and Linux virtual machines", r"\bvm\b|oracle|linux|ampere"),
    ("Mouse and trackball", r"mouse|trackball"),
    ("Mac computers, displays and GPU", r"\bmac\b|macbook|display|monitor|gpu|apple silicon"),
]


def gen_hardware(live, retired, planned, guides, by_repo):
    fam = defaultdict(lambda: defaultdict(list))
    order = [t for t, _ in HW_FAMILIES] + ["Other devices"]
    for r in live + retired + planned:
        for h in r["hardware"]:
            title = "Other devices"
            for t, rx in HW_FAMILIES:
                if re.search(rx, h.lower()):
                    title = t
                    break
            fam[title][r["repo"]].append(h)
    byx = {r["repo"]: r for r in live + retired + planned}
    # a guide goes to the device group with the best keyword match
    ggroup = defaultdict(list)
    for g in guides:
        kws = [k.lower() for k in g.get("applies_to", [])]
        best, score = None, 0
        for t in order:
            sc = sum(5 for k in kws if k in t.lower())
            sc += sum(1 for repo, hs in fam.get(t, {}).items() if any(k in " ".join(hs).lower() for k in kws))
            if sc > score:
                best, score = t, sc
        if best:
            ggroup[best].append(g)
    L = ["# Hardware: which apps drive which device", "",
         "Device families first, then the apps that name a device of that family (live, then planned, then retired). The exact device wording from each card is in brackets.", ""]
    for t in order:
        if t not in fam:
            continue
        L += ["## " + t, ""]
        for g in ggroup.get(t, []):
            L += guide_md(g, by_repo, "apps/", "###")
        for repo in sorted(fam[t], key=lambda x: (1 if byx[x].get("_planned") else 0, 1 if is_retired(byx[x]) else 0, byx[x]["name"].lower(), x)):
            L.append("- %s (%s)" % (card_link(byx[repo]), esc("; ".join(fam[t][repo]))))
        L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Modules
# ---------------------------------------------------------------------------
MOD_THEMES = [
    ("Remote door, ports and control API", r"\bdoor\b|/health|/api|\bports?\b|remote control|control api|local api|\bapi server|http server"),
    ("Updater, installer and releases", r"updat|install|release|version"),
    ("AI providers, agents and prompts", r"groq|claude|\bllm\b|\bgpt\b|\bai\b|agent|\bmodel|prompt|openai|gemini|anthropic|speechify|hume"),
    ("Speech, transcription and voice", r"whisper|transcri|speech|voice|\btts\b|\bstt\b|dictat|speak|subtitle|caption"),
    ("MIDI, OSC and mixers", r"midi|\bosc\b|mixer|\bcq\b|ableton|\boxi\b|mackie|launchkey"),
    ("Audio, music and DJ", r"audio|sound|music|\bbpm\b|beat|\bsong|loop|playback|sample|\btone|waveform|spectr|\bmix|pitch|chord"),
    ("Camera, video and NDI", r"camera|video|\bndi\b|webcam|sony|\bptp\b|stream|frame|capture|resolve|ffmpeg|\bhls\b|\bimage|screenshot|3d|render|blender"),
    ("Bluetooth, USB and devices", r"\bble\b|bluetooth|\busb\b|\bhid\b|\badb\b|serial|keyboard|g815|device|gps|sensor|shizuku"),
    ("Android and Termux", r"android|termux|kotlin|\bapk\b|gradle"),
    ("Mac automation and accessibility", r"accessib|hammerspoon|applescript|macro|\bax\b|launchd|menu bar|swift|window|hotkey|clipboard|\bdock"),
    ("Networking, sync and remote machines", r"network|tailscale|\bssh\b|wi-?fi|http|websocket|\bsync|upload|\bvpn\b|proxy|router|server|download|\bvnc\b|cloud"),
    ("UI kits, pages and design", r"\bui\b|\bview|button|theme|css|html|\bpage|design|layout|panel|menu|screen|display|overlay|font|map|chart"),
    ("Files, data and text", r"file|json|csv|database|search|pars|text|\blog|backup|export|import|zip|index|registry|schema"),
]


def mod_theme(m):
    s = (m["path"] + " " + m["what"]).lower()
    for t, rx in MOD_THEMES:
        if re.search(rx, s):
            return t
    return "Other"


def gen_modules(cards):
    by_theme = defaultdict(list)
    for r in cards:
        for m in r["reusable_modules"]:
            by_theme[mod_theme(m)].append((r, m))
    total = sum(len(v) for v in by_theme.values())
    L = ["# Reusable modules", "",
         "%d code modules in %d repositories that another app could copy instead of rewriting. Each row: what it does, the repository card, and the path inside the repository. Private repositories are marked; ask Marko for access or copy the idea. Modules of retired apps are marked (retired)." % (
             total, len({r["repo"] for v in by_theme.values() for r, _ in v})), ""]
    for t, _ in MOD_THEMES + [("Other", "")]:
        rows = by_theme.get(t)
        if not rows:
            continue
        rows.sort(key=lambda x: (x[0]["repo"].lower(), x[1]["path"]))
        L += ["## %s (%d)" % (t, len(rows)), "", "| What it does | Repo | Path |", "|---|---|---|"]
        for r, m in rows:
            repo = "%s%s" % (card_link_plain(r), " (private)" if r["visibility"] == "private" else "")
            L.append("| %s | %s | %s |" % (cell(m["what"] or "(no description)"), repo, cs(m["path"], True)))
        L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Mermaid: mind map and connection graphs
# ---------------------------------------------------------------------------
def cat_sections(recs):
    for slug, title in CATS:
        rs = sorted([r for r in recs if r["category"] == slug], key=lambda r: (is_retired(r), r["name"].lower(), r["repo"]))
        if rs:
            yield slug, title, rs


def mindmaps(live, retired, planned):
    groups = []
    for slug, title in CATS:
        leaves = [plain_name(r) for r in live if r["category"] == slug]
        leaves += [plain_name(r) for r in planned if r["category"] == slug]
        leaves += [plain_name(r) for r in retired if r["category"] == slug]
        if not leaves:
            continue
        for i in range(0, len(leaves), 40):
            part = leaves[i:i + 40]
            label = title if len(leaves) <= 40 else "%s %d" % (title, i // 40 + 1)
            groups.append((label, part))
    diagrams, cur, n = [], [], 0
    for label, part in groups:
        if cur and n + len(part) > 60:
            diagrams.append(cur)
            cur, n = [], 0
        cur.append((label, part))
        n += len(part)
    if cur:
        diagrams.append(cur)
    out = []
    for d in diagrams:
        lines = ["mindmap", "  root((Mantra apps))"]
        for label, part in d:
            lines.append("    " + mm_label(label, 60))
            for x in part:
                lines.append("      " + x)
        out.append("\n".join(lines))
    return out


def graph_src(items, label_of, stubs=(), extra_nodes=None):
    """items: list of (src, dst, label, arrow). Nodes are keys; label_of(key) gives the text."""
    ids = {}
    order = []
    for a, b, l, ar in items:
        for x in (a, b):
            if x not in ids:
                ids[x] = "n%d" % len(ids)
                order.append(x)
    lines = ["graph LR"]
    for x in order:
        lines.append('  %s["%s"]' % (ids[x], label_of(x)))
    for a, b, l, ar in items:
        lines.append('  %s %s|"%s"| %s' % (ids[a], ar, l, ids[b]))
    st = [ids[x] for x in order if x in stubs]
    if st:
        lines += ["  classDef stub stroke-dasharray: 3 3", "  class %s stub" % ",".join(st)]
    return "\n".join(lines)


def gen_connections(cards, planned, edges, by_repo):
    by_all = dict(by_repo)
    lab = lambda x: plain_name(by_all[x], 36)
    L = ["# Connections: who talks to whom", "",
         "Solid arrow: the app uses (depends on) the other. Dotted arrow: it talks to or is controlled by the other. Only edges where both ends are apps on this map are drawn. "
         "One graph per category (dashed boxes are apps of other categories, shown only as stubs), then the most connected apps, then the planned Light Control. The full edge list is at the end.", ""]
    L += ["## Most connected apps", ""]
    deg = Counter()
    for a, b, l in edges:
        deg[a] += 1
        deg[b] += 1
    hubs = sorted(deg, key=lambda x: (-deg[x], by_repo[x]["name"].lower()))[:15]
    hs = set(hubs)
    he = [(a, b, l, "-->" if l == "uses" else "-.->") for a, b, l in edges if a in hs and b in hs]
    if he:
        L += ["```mermaid", graph_src(he, lambda x: "%s (%d)" % (plain_name(by_repo[x], 30), deg[x])), "```", ""]
    L += ["| Links | App |", "|---|---|"] + ["| %d | %s |" % (deg[h], card_link(by_repo[h])) for h in hubs] + [""]
    for slug, title in CATS:
        es = [(a, b, l, "-->" if l == "uses" else "-.->") for a, b, l in edges
              if by_repo[a]["category"] == slug or by_repo[b]["category"] == slug]
        if not es:
            continue
        stubs = {x for a, b, l, ar in es for x in (a, b) if by_repo[x]["category"] != slug}
        L += ["## " + title, "", "```mermaid", graph_src(es, lab, stubs), "```", ""]
    for p in planned:
        items, ext = [], {}
        for e in p["_edges"]:
            lbl = mq_label(e["label"] + (", " + e["port"] if e.get("port") else ""))
            tgt = e["to"] if e.get("to") else "ext:" + e["external"]
            if e.get("external"):
                ext[tgt] = e["external"]
            if e["dir"] == "out":
                items.append((p["repo"], tgt, lbl, "-.->"))
            elif e["dir"] == "in":
                items.append((tgt, p["repo"], lbl, "-.->"))
            else:
                items.append((p["repo"], tgt, lbl, "<-.->"))
        by_all2 = dict(by_repo)
        by_all2[p["repo"]] = p

        def plab(x, by_all2=by_all2, ext=ext):
            if x in ext:
                return mm_label(ext[x], 40)
            return plain_name(by_all2[x], 36)
        L += ["## Planned: %s" % esc(p["name"]), "",
              "%s is planned, not built (kickoff prompt: [%s](%s)). Arrows show who calls whom; labels give the role and the port." % (esc(p["name"]), p["_prompt"], p["_prompt"]), "",
              "```mermaid", graph_src(items, plab, {p["repo"]}), "```", ""]
        L += ["- " + edge_text(e, by_repo) for e in p["_edges"]] + [""]
    L += ["## Edge list", "", "Format: app -> what it uses (u) or talks to (t).", ""]
    out = defaultdict(list)
    for a, b, l in edges:
        out[a].append((b, l))
    for a in sorted(out, key=lambda x: by_repo[x]["name"].lower()):
        L.append("- %s -> %s" % (card_link_plain(by_repo[a]), ", ".join(
            "%s (%s)" % (card_link_plain(by_repo[b]), "u" if l == "uses" else "t") for b, l in out[a])))
    return "\n".join(L)


def gen_mindmap(live, retired, planned):
    L = ["# Mind map of everything", "",
         "The brain as pictures first, then as an outline. Every leaf is an app or tool on this map; the outline links to its card. Planned apps are marked PLANNED, retired apps RETIRED.", ""]
    for i, src in enumerate(mindmaps(live, retired, planned), 1):
        L += ["## Diagram %d" % i, "", "```mermaid", src, "```", ""]
    L += ["## Outline", ""]
    allr = live + retired
    for slug, title, rs in cat_sections(allr):
        L += ["### " + title, ""]
        for r in rs:
            tail = "" if norm_key(r["name"]) == norm_key(r["repo"]) or norm_key(r["name"]) in CTX["collide"] else " (%s)" % cs(r["repo"])
            L.append("- %s%s%s" % (card_link(r), tail, (" - " + esc(r["one_line"])) if r["one_line"] else ""))
        for p in planned:
            if p["category"] == slug:
                L.append("- %s%s - %s [kickoff prompt](%s)" % (card_link(p), "", esc(p["one_line"]), p["_prompt"]))
        L.append("")
    return "\n".join(L)


# ---------------------------------------------------------------------------
# README and STATUS
# ---------------------------------------------------------------------------
README_EXAMPLES = ["sony", "midi", "transcribe", "light", "neewer", "play-loop", "8965"]


def gen_readme(cards, live, retired, planned, gaps, meta, empties):
    apps = [r for r in live if r["kind"] == "app"]
    lv = Counter(r["control"]["level"] for r in live)
    plat = Counter(p for r in live for p in r["platforms"])
    with_api = len(live) - lv["none"]
    others = [x for x in CTX["ports"].get("8965", []) if x != "MANTRA_ROOM"]
    port_note = ("; that number is also quoted for %s, so confirm with `mantra-ports scan`" % ", ".join(
        card_link(CTX["by"][x]) for x in others)) if others else ""
    grep_in = "CAPABILITIES.md capabilities/ KEYWORDS.md" if CTX.get("split") else "CAPABILITIES.md KEYWORDS.md"
    L = ["# APPS_MIND_MAP", "",
         "A map of every app, tool and reusable code module Marko Bosko has built, in one place, written for an AI session that has a task in hand.",
         "Each repository has one card in `apps/`. Each card says what the app does, when to ask for it, how to control it from outside, and which code in it can be copied.",
         "The apps are built so that other programs can drive them: a local HTTP door, a command line or a Python client. That is how the apps are chained into one ecosystem.",
         "Code that already exists is reused as modules instead of written again, so MODULES.md lists what can be lifted from where.",
         "Everything except `data/` and `prompts/` is generated from `data/apps.json` by `tools/build_map.py`. Edit the data, not the pages.",
         "", "## How an AI uses this map", "",
         "1. **Find the task.** Search first: `grep -ri <word> %s` (a device, a port, an action name or a task word), or open `index.html` and type it. Examples that work: %s. "
         "Then read %s: its task lines are grouped by category, and the first line of each app carries the port and a working example call. "
         "A \"Which one to pick\" guide at the top of a category chooses between look-alike apps. If the search ends at \"Not built yet\", no app does the job: build it as a new app. For a device see [HARDWARE.md](HARDWARE.md)." % (
             grep_in, ", ".join("`%s`" % w for w in README_EXAMPLES), "the matching file in `capabilities/` (or [CAPABILITIES.md](CAPABILITIES.md))" if CTX.get("split") else "[CAPABILITIES.md](CAPABILITIES.md)"),
         "2. **Open the app card** (`apps/REPO.md`) only if you need the full action list, the evidence or the notes.",
         "3. **Call the app through its API.** The standard protocol (the Mantra Door pattern):",
         "   - the app listens on `127.0.0.1` only, on a port claimed in `MANTRA_PORTS` under its id (for example `meditation-room` is 8965%s);" % port_note,
         "   - `GET /health` answers `{app, name, version, pid}`; `GET /api` lists the actions, each with a one-sentence `does`; `POST /api/<action>` takes a JSON body and answers `{ok: true, result}` or `{ok: false, error}`; `GET /api/state` is optional;",
         "   - from Python use `mantra_remote.py` (`remote.call(\"meditation-room\", \"stop\")`); it talks to the Mantra Door on the Mac, which starts a stopped app, forwards the call and needs the door token (never printed or committed);",
         "   - a call needs no token on `127.0.0.1` for an app's own door; other routes use the `X-Mantra-Token` header;",
         "   - Android and Termux have no common door: Android apps use adb forwards, intents or an accessibility door (for example port 8790), Termux apps write their live port to `~/.mantra/ports/<command>`. Each card says which.",
         "   - [CONTROL_API.md](CONTROL_API.md) lists every app that can be driven, grouped by how (door, http, other protocols, command line, adb, accessibility).",
         "4. **If no app does it**, open [MODULES.md](MODULES.md): the code to copy (audio, camera, BLE and USB, UI kits, networking, AI providers, updater and more). Copy the module, do not rewrite it.",
         "5. **See who talks to whom** in [CONNECTIONS.md](CONNECTIONS.md) and the whole picture in [MIND_MAP.md](MIND_MAP.md).",
         "6. **If a new app is built, add its card:** add a record to `data/apps.json` (same keys as the other records), run `python3 tools/build_map.py`, commit the changed files. An app that is not on the map is not finished.",
         "", "## How to claim a port for a new app", "",
         "- Ask the registry for the next free number: `mantra-ports next` (from the MANTRA_PORTS card); write it in the app's README.",
         "- In the app's server claim it: `PORT = ports.claim('<app-id>', <number>)` (Python `ports.py`, Swift `Ports.swift`, Lua `ports.lua`). It takes that number if free, else the next free one, and records it.",
         "- Clients ask `ports.url('<app-id>', <number>)` for the live address instead of hard-coding the number.",
         "- Before a release run `mantra-ports scan` (no port named twice) and `mantra-ports check` (names the holder of a clash).",
         "", "## Rules of this ecosystem", "",
         "- Every app ships the control API from its first version: `/health`, `/api`, `POST /api/<action>` on a claimed port.",
         "- Reuse before writing: look in this map for an app to call or code to copy before building anything.",
         "- Work in modules: a feature that another app could use lives in a module with its own path and one clear job.",
         "- One branch, `main`. Whole-number versions, visible in the app.",
         "- A planner model plans, briefs and scores the result; workers on lower models build and test.",
         "- Secrets stay in local files, never in a repository. This repository holds no secrets, addresses or personal data.",
         "- The full rules live in the private `MANTRA_MANIFEST` repository; they are not repeated here.",
         "", "## The numbers", "",
         "- %d live repositories have a card (%d are apps; the rest are tools, libraries, websites, guides, data and config); %d more are retired and marked so." % (len(live), len(apps), len(retired)),
         "- %d of the live ones can be driven from outside (%d at the standard door level)." % (with_api, lv["door"]),
         "- By control level: " + ", ".join("%s %d" % (k, lv[k]) for k in LEVELS if lv[k]) + ".",
         "- By platform (a repository can be on several): " + ", ".join("%s %d" % (p, plat[p]) for p in PLATFORMS if plat[p]) + ".",
         "- %d empty repositories have no card; %d were left out for privacy (see [STATUS.md](STATUS.md))." % (len(empties), meta.get("excluded", 0))]
    L += ["", "## Not built yet", "", "A search that ends here means no app does the job yet.", ""]
    for g in gaps:
        L.append("- **%s** (%s): %s" % (esc(g["need"]), g["status"], esc(g.get("note", ""))))
    for p in planned:
        L.append("- **%s** (planned): %s [kickoff prompt](%s), [card](apps/%s.md)" % (esc(p["name"]), esc(p["one_line"]), p["_prompt"], p["repo"]))
    L += ["", "## Categories", ""]
    for slug, title, rs in cat_sections(live):
        L.append("- [%s](%s): %d" % (title, cat_target(slug), len(rs)))
    L += ["", "## Files", "",
          "- [MIND_MAP.md](MIND_MAP.md): the brain as diagrams and as an outline.",
          "- [CAPABILITIES.md](CAPABILITIES.md): task index" + (" (index of categories; the task lines are in `capabilities/`)." if CTX.get("split") else "."),
          "- [KEYWORDS.md](KEYWORDS.md): alphabetical keyword index (words, ports, action names).",
          "- [CONTROL_API.md](CONTROL_API.md): how to call each app, plus the apps still without an API.",
          "- [HARDWARE.md](HARDWARE.md): device to apps.",
          "- [MODULES.md](MODULES.md): reusable code.",
          "- [CONNECTIONS.md](CONNECTIONS.md): who talks to whom.",
          "- [STATUS.md](STATUS.md): housekeeping lists.",
          "- `index.html`: search page.",
          "- `apps/`: one card per repository.",
          "- `data/apps.json`: the single source of truth. `data/planned.json`: apps planned but not built. `data/guides.json`: which-one-to-pick guides and gaps. `data/repos.tsv`: repository metadata. `prompts/`: kickoff prompts for new apps.",
          "- `tools/build_map.py`: rebuilds every generated file (`--check` exits 1 if a generated file is out of date). `tools/import_catalog.py`: one-off import of a catalog folder into `data/apps.json` with a local exclude file.",
          "", "## Keeping the map current", "",
          "1. Edit `data/apps.json` (or `data/planned.json`, `data/guides.json`).",
          "2. Run `python3 tools/build_map.py` (Python 3, standard library only). It rewrites all generated files and checks that every link resolves.",
          "3. Run it twice: the second run must change nothing. `python3 tools/build_map.py --check` does that check without writing.",
          "4. When a planned app is built, move it from `data/planned.json` into `data/apps.json` as a full record."]
    return "\n".join(L)


def gen_status(recs, cards, live, retired, empties, meta, edges):
    L = ["# Status and housekeeping", ""]
    lv = Counter(r["control"]["level"] for r in live)
    L += ["## Counts", "",
          "- Records read from the catalog: %d" % meta.get("records_in", len(recs)),
          "- Left out for privacy: %d" % meta.get("excluded", 0),
          "- Empty repositories, no card: %d" % len(empties),
          "- Cards written: %d (%d live, %d retired)" % (len(cards), len(live), len(retired)),
          "- Live cards by control level: " + ", ".join("%s %d" % (k, lv[k]) for k in LEVELS if lv[k]), ""]
    if empties:
        L += ["## Empty repositories", ""] + ["- %s (%s)" % (cs(r["repo"]), r["visibility"]) for r in empties] + [""]
    if retired:
        L += ["## Retired or archived, and what replaced them", ""]
        for r in retired:
            flag, rep, sent = CTX["retired"][r["repo"]]
            s = "- %s" % card_link(r)
            if rep:
                s += ": replaced by %s" % card_link(CTX["by"][rep])
            elif sent:
                s += ": " + esc(tidy(sent))
            L.append(s)
        L.append("")
    low = [r for r in cards if r["confidence"] == "low"]
    if low:
        L += ["## Low-confidence records to re-read", ""] + ["- %s: %s" % (card_link(r), esc(r["one_line"])) for r in low] + [""]
    L += ["## Port collisions", ""]
    if CTX["ports"]:
        L += ["Same port number written in more than one card (may be different machines; each card carries a warning; check with `mantra-ports scan`):", ""]
        for p in sorted(CTX["ports"]):
            L.append("- %s: %s" % (p, ", ".join(card_link(CTX["by"][x]) for x in CTX["ports"][p])))
        L.append("")
    note_rx = re.compile(r"collision|collide|clash|same port|also used|also quoted|conflict", re.I)
    hits = [(r, [s for s in sentences(r["notes"]) if note_rx.search(s)]) for r in cards]
    hits = [(r, s) for r, s in hits if s]
    if hits:
        L += ["Mentioned in notes:", ""] + ["- %s: %s" % (card_link(r), esc(tidy(" ".join(s)))) for r, s in hits] + [""]
    dup_rx = re.compile(r"duplicate|copy of|twin|supersed|same code|fork of|replaced by|replaces|older version|newer version", re.I)
    d = [(r, [s for s in sentences(r["notes"]) if dup_rx.search(s)]) for r in cards]
    d = [(r, s) for r, s in d if s]
    if d:
        L += ["## Duplicates and superseded pairs", ""] + ["- %s: %s" % (card_link(r), esc(tidy(" ".join(s)))) for r, s in d] + [""]
    mis = [r for r in cards if r["control"]["has_api"] == "yes" and r["control"]["level"] == "none"]
    mis2 = [r for r in cards if r["control"]["has_api"] != "yes" and r["control"]["level"] != "none"]
    if mis or mis2:
        L += ["## Catalog judgement and control level disagree", ""]
        if mis:
            L += ["Catalog says API yes, evidence gives level none:", ""] + ["- " + card_link(r) for r in mis] + [""]
        if mis2:
            L += ["Catalog says no or unknown, but actions are listed (level shown):", ""] + ["- %s (%s)" % (card_link(r), r["control"]["level"]) for r in mis2] + [""]
    stale_rx = re.compile(r"may not (?:exist|be served)|older (?:engine|flask)", re.I)
    st = [(r, [x for x in sentences(r["notes"]) if stale_rx.search(x)]) for r in live if r["control"]["level"] in ("door", "http")]
    st = [(r, x) for r, x in st if x]
    if st:
        L += ["## Control level may be out of date", "",
              "Level is http or door, but the notes say the API may belong to an older version of the app:", ""]
        L += ["- %s (%s): %s" % (card_link(r), r["control"]["level"], esc(tidy(" ".join(x)))) for r, x in st] + [""]
    ub = [r for r in cards if r["unmerged_branches"]]
    if ub:
        L += ["## Repositories with unmerged branches", ""] + ["- %s: %d" % (card_link(r), r["unmerged_branches"]) for r in ub] + [""]
    return "\n".join(L)


# ---------------------------------------------------------------------------
# index.html
# ---------------------------------------------------------------------------
INDEX_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>APPS_MIND_MAP search</title>
<style>
:root{--bg:#fafaf7;--fg:#1d1d1b;--mut:#5f5f58;--card:#fff;--line:#d9d8cf;--acc:#1f5fa8;--ok:#1b6e3c;--tag:#eceae0;--warn:#8a4b00}
@media (prefers-color-scheme:dark){:root{--bg:#15161a;--fg:#e8e8e3;--mut:#a0a09a;--card:#1e2026;--line:#363944;--acc:#7db3f0;--ok:#6fcf97;--tag:#2a2d36;--warn:#f0b36a}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:900px;margin:0 auto;padding:16px}
h1{font-size:1.3rem;margin:.2em 0}
p.lead{color:var(--mut);margin:.2em 0 1em}
.bar{display:grid;gap:8px;grid-template-columns:1fr 1fr 1fr;margin-bottom:8px}
.bar input[type=search]{grid-column:1/-1}
input,select{font:inherit;padding:10px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);width:100%;min-width:0}
label.chk{display:flex;align-items:center;gap:8px;grid-column:1/-1}
label.chk input{width:auto}
#count{color:var(--mut);margin:8px 0}
.card,.note{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:8px 0;overflow-wrap:anywhere;min-width:0}
.note{padding:10px 12px}
.note h2{font-size:.95rem;margin:0 0 6px}
.note ul{margin:0;padding-left:20px}
.head{display:block;width:100%;text-align:left;background:none;border:0;color:inherit;font:inherit;padding:12px;cursor:pointer;overflow-wrap:anywhere}
.head:focus-visible{outline:2px solid var(--acc);border-radius:10px}
.name{font-weight:650}
.repo{color:var(--mut);font-size:.85rem;margin-left:6px}
.one{display:block;margin-top:2px}
.tags{margin-top:6px;display:flex;flex-wrap:wrap;gap:6px}
.tag{background:var(--tag);border-radius:999px;padding:1px 9px;font-size:.78rem}
.tag.api{color:var(--ok);font-weight:600}
.tag.planned,.tag.retired{color:var(--warn);font-weight:600}
.card.retired{opacity:.8}
.body{padding:0 12px 12px;border-top:1px solid var(--line)}
.body h3{font-size:.85rem;text-transform:uppercase;letter-spacing:.04em;color:var(--mut);margin:12px 0 4px}
.body ul{margin:0;padding-left:20px}
pre{background:var(--tag);padding:8px;border-radius:6px;overflow:auto;white-space:pre-wrap;word-break:break-word;margin:4px 0}
code{word-break:break-word}
a{color:var(--acc)}
@media (max-width:560px){.bar{grid-template-columns:1fr}}
</style>
</head>
<body>
<main>
<h1>APPS_MIND_MAP</h1>
<p class="lead">Search every app, tool and module by task, device, port or action name: sony, midi, light control, 8965, play-loop.</p>
<div class="bar">
<input id="q" type="search" placeholder="Search name, task, hardware, port, action..." aria-label="Search" autocomplete="off">
<select id="cat" aria-label="Category"></select>
<select id="plat" aria-label="Platform"></select>
<select id="lvl" aria-label="Control level"></select>
<label class="chk"><input id="api" type="checkbox"> Only apps that have an API</label>
</div>
<div id="count" aria-live="polite"></div>
<div id="notes"></div>
<div id="list"></div>
</main>
<script id="data" type="application/json">__DATA__</script>
<script>
(function(){
"use strict";
var D=JSON.parse(document.getElementById("data").textContent);
var RECS=D.records,GAPS=D.gaps,GUIDES=D.guides;
var q=document.getElementById("q"),cat=document.getElementById("cat"),plat=document.getElementById("plat"),lvl=document.getElementById("lvl"),api=document.getElementById("api"),list=document.getElementById("list"),count=document.getElementById("count"),notes=document.getElementById("notes");
function opt(sel,v,t){var o=document.createElement("option");o.value=v;o.textContent=t;sel.appendChild(o);}
opt(cat,"","All categories");D.categories.forEach(function(c){opt(cat,c[0],c[1]);});
opt(plat,"","All platforms");D.platforms.forEach(function(p){opt(plat,p,p);});
opt(lvl,"","Any control level");D.levels.forEach(function(l){opt(lvl,l,l);});
function lc(a){return a.join(" ").toLowerCase();}
RECS.forEach(function(r){
 r._n=(r.name+" "+r.repo+" "+r.aliases.join(" ")).toLowerCase();
 r._t=lc(r.tasks.concat(r.kw));
 r._h=[r._n,r._t,r.one_line,lc(r.does),lc(r.hardware),r.category_title,lc(r.platforms),String(r.port||""),lc(r.control.actions),r.control.how_to_call||"",lc(r.control.type),r.notes,r.control.before,r.control.protocol,r.control.examples.map(function(x){return x["for"]+" "+x.call;}).join(" ")].join(" \n ").toLowerCase();
});
GAPS.forEach(function(g){g._h=(g.need+" "+(g.note||"")+" "+g.status+" "+(g.keywords||[]).join(" ")).toLowerCase();});
GUIDES.forEach(function(g){g._h=(g.title+" "+g.applies_to.join(" ")+" "+g.text+" "+g.picks.map(function(p){return p["for"]+" "+p.use+" "+(p.how||"");}).join(" ")).toLowerCase();});
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e;}
function section(body,title,items,pre){
 if(!items||!items.length)return;
 body.appendChild(el("h3",null,title));
 if(pre){var p=el("pre");p.textContent=items;body.appendChild(p);return;}
 var u=el("ul");items.forEach(function(i){u.appendChild(el("li",null,i));});body.appendChild(u);
}
function build(r){
 var card=el("div","card"+(r.state==="retired"?" retired":"")),btn=el("button","head");btn.type="button";btn.setAttribute("aria-expanded","false");
 btn.appendChild(el("span","name",r.name));btn.appendChild(el("span","repo",r.repo));
 btn.appendChild(el("span","one",r.one_line));
 var tags=el("div","tags"),lv=r.control.level;
 if(r.state==="planned")tags.appendChild(el("span","tag planned","planned"));
 if(r.state==="retired")tags.appendChild(el("span","tag retired","retired"));
 if(r.state!=="planned")tags.appendChild(el("span","tag"+(lv!=="none"?" api":""),lv==="none"?"no API":"API: "+lv+(r.port?" "+r.port:"")));
 tags.appendChild(el("span","tag",r.category_title));
 r.platforms.forEach(function(p){tags.appendChild(el("span","tag",p));});
 if(r.visibility==="private")tags.appendChild(el("span","tag","private"));
 btn.appendChild(tags);card.appendChild(btn);
 var body=null;
 btn.addEventListener("click",function(){
  if(body){body.hidden=!body.hidden;btn.setAttribute("aria-expanded",String(!body.hidden));return;}
  body=el("div","body");
  if(r.state==="planned")section(body,"Planned, not built",["No repository and no API yet. See the kickoff prompt."].concat(r.links));
  if(r.state==="retired")section(body,"Retired - do not use",[r.retired_note||"See the card."]);
  section(body,"What it can do",r.does);
  section(body,"Ask for it when",r.tasks);
  var c=r.control;
  if(r.state!=="planned"){
   var info=["Level: "+c.level+" (type: "+(c.type.join(", ")||"unknown")+")"];
   if(c.port)info.push("Port: "+c.port);
   section(body,"How to control it",info);
   if(c.actions.length)section(body,"Actions",c.actions);
   if(c.protocol)section(body,"Protocol",[c.protocol]);
   if(c.before)section(body,"Before you call",[c.before]);
   if(c.how_to_call)section(body,"Example",c.how_to_call,true);
   if(c.examples.length)section(body,"More calls",c.examples.map(function(x){return x["for"]+": "+x.call;}));
   if(c.evidence&&c.evidence!=="none found")section(body,"Evidence",[c.evidence]);
  }
  section(body,"Hardware",r.hardware);
  section(body,"Code worth reusing",r.reusable_modules.map(function(m){return m.path+": "+m.what;}));
  if(r.notes)section(body,"Notes",[r.notes]);
  body.appendChild(el("h3",null,"Links"));
  var p=el("p"),a1=el("a",null,"Full card");a1.href="apps/"+encodeURIComponent(r.repo)+".md";p.appendChild(a1);
  if(r.state==="planned"){p.appendChild(document.createTextNode(" | "));var a3=el("a",null,"Kickoff prompt");a3.href=r.prompt;p.appendChild(a3);}
  else{p.appendChild(document.createTextNode(" | "));var a2=el("a",null,"GitHub repo");a2.href="https://github.com/"+D.owner+"/"+encodeURIComponent(r.repo);p.appendChild(a2);}
  body.appendChild(p);card.appendChild(body);btn.setAttribute("aria-expanded","true");
 });
 return card;
}
var CARDS=RECS.map(build);
function note(title,items){
 var n=el("div","note");n.appendChild(el("h2",null,title));
 var u=el("ul");items.forEach(function(t){u.appendChild(el("li",null,t));});n.appendChild(u);notes.appendChild(n);
}
function run(){
 var terms=q.value.toLowerCase().split(/\s+/).filter(Boolean);
 var out=[],pick={};
 var um0=terms.length?GUIDES.filter(function(g){return terms.every(function(t){return g._h.indexOf(t)>=0;});}):[];
 um0.forEach(function(g){g.picks.forEach(function(p){pick[p.use]=1;});});
 RECS.forEach(function(r,i){
  if(cat.value&&r.category!==cat.value)return;
  if(plat.value&&r.platforms.indexOf(plat.value)<0)return;
  if(lvl.value&&r.control.level!==lvl.value)return;
  if(api.checked&&r.control.level==="none")return;
  var s=0;
  for(var k=0;k<terms.length;k++){
   if(r._h.indexOf(terms[k])<0)return;
   s+=r._n.indexOf(terms[k])>=0?100:(r._t.indexOf(terms[k])>=0?40:10);
  }
  if(r.control.level!=="none")s+=5;
  if(pick[r.repo])s+=60;
  if(r.state==="retired")s-=1000;
  out.push([s,i]);
 });
 out.sort(function(a,b){return b[0]-a[0]||a[1]-b[1];});
 list.textContent="";notes.textContent="";
 out.forEach(function(o){list.appendChild(CARDS[o[1]]);});
 var tail="";
 if(terms.length){
  var gm=GAPS.filter(function(g){return terms.every(function(t){return g._h.indexOf(t)>=0;});});
  var um=um0;
  if(!out.length)notes.appendChild(el("div","note",'No app on the map matches "'+q.value+'".'));
  if(gm.length)note("Not built yet",gm.map(function(g){return g.need+" ("+g.status+"): "+(g.note||"");}));
  if(um.length)note("Which one to pick",um.map(function(g){return g.title+": "+g.picks.map(function(p){return p["for"]+" -> "+p.use;}).join("; ");}));
 }
 count.textContent=out.length+" of "+RECS.length+" entries";
}
[q,cat,plat,lvl].forEach(function(e){e.addEventListener("input",run);});
api.addEventListener("change",run);
run();
})();
</script>
</body>
</html>
"""


def gen_index(live, retired, planned, guides, gaps, by_repo):
    recs = []
    for r in live + retired + planned:
        c = r["control"]
        flag, rep, sent = CTX["retired"].get(r["repo"], (False, None, None))
        o = {
            "repo": r["repo"], "name": dname(r, False), "aliases": r["aliases"], "visibility": r["visibility"],
            "category": r["category"], "category_title": CAT_TITLE[r["category"]], "platforms": r["platforms"],
            "state": "planned" if r.get("_planned") else ("retired" if flag else "live"),
            "one_line": r["one_line"], "does": r["does"], "tasks": r["tasks"], "hardware": r["hardware"],
            "control": {"level": c["level"], "type": c["type"], "port": c["port"], "actions": c["actions"],
                        "how_to_call": c["how_to_call"], "evidence": c["evidence"],
                        "before": c.get("before") or "", "protocol": c.get("protocol") or "",
                        "examples": c.get("examples") or []},
            "port": first_int(c["port"]) if c["level"] != "none" else None,
            "reusable_modules": r["reusable_modules"], "notes": r["notes"],
            "kw": list(r.get("_keywords", [])), "links": [], "prompt": r.get("_prompt", ""),
            "retired_note": ("Replaced by %s. " % by_repo[rep]["name"] if rep else "") + (tidy(sent) if sent else ""),
        }
        if r.get("_planned"):
            o["links"] = [re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", edge_text(e, by_repo)).replace("`", "") for e in r["_edges"]]
        recs.append(o)
    payload = {"owner": OWNER, "categories": CATS, "platforms": PLATFORMS, "levels": LEVELS, "records": recs,
              "gaps": gaps, "guides": [{"title": g["title"], "applies_to": g.get("applies_to", []), "text": g.get("text", ""),
                                        "picks": g.get("picks", [])} for g in guides]}
    js = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    js = js.replace("</", "<\\/").replace("<!--", "<\\!--").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    return INDEX_TEMPLATE.replace("__DATA__", js)


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------
def check_text(cards):
    bad = []
    for r in cards:
        o = r["one_line"]
        if len(o) > MAX_ONE_LINE or o.endswith("..."):
            bad.append("%s: one_line is %d chars or ends with '...'" % (r["repo"], len(o)))
    return bad


def check_links(files):
    bad = []
    anchors = {}

    def text_of(path):
        if path in files:
            return files[path]
        with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
            return fh.read()

    def exists(path):
        return path in files or os.path.exists(os.path.join(ROOT, path))

    def anchors_of(path):
        if path not in anchors:
            a, inc = set(), False
            for line in text_of(path).split("\n"):
                if line.startswith("```"):
                    inc = not inc
                elif not inc and line.startswith("#"):
                    a.add(gh_anchor(line.lstrip("#")))
            anchors[path] = a
        return anchors[path]

    for f in sorted(files):
        if not f.endswith(".md"):
            continue
        base = os.path.dirname(f)
        text = re.sub(r"```.*?```", "", files[f], flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            t = m.group(1)
            if t.startswith(("http://", "https://", "mailto:")):
                continue
            p, _, frag = t.partition("#")
            target = os.path.normpath(os.path.join(base, p)) if p else f
            if not exists(target):
                bad.append("%s -> %s" % (f, t))
            elif frag and target.endswith(".md") and frag not in anchors_of(target):
                bad.append("%s -> %s (anchor)" % (f, t))
    return bad


def check_privacy(files):
    bad = []
    for f, t in files.items():
        if EMAIL_RE.search(t):
            bad.append("%s: e-mail pattern" % f)
        for m in IPV4_RE.finditer(t):
            if m.group(0) not in ("127.0.0.1", "0.0.0.0"):
                bad.append("%s: ip %s" % (f, m.group(0)))
    return bad


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def generate():
    recs = load_json("apps.json", None)
    if recs is None:
        sys.exit("data/apps.json missing; run tools/import_catalog.py first")
    meta = load_json("meta.json", {})
    planned_raw = load_json("planned.json", [])
    gdata = load_json("guides.json", {})
    guides, gaps = gdata.get("guides", []), gdata.get("gaps", [])
    recs = [normalise_record(r) for r in recs]
    recs.sort(key=lambda r: r["repo"].lower())
    low = [r["repo"].lower() for r in recs]
    assert len(set(low)) == len(low), "repo names collide when lower-cased"
    empties = [r for r in recs if r["kind"] == "empty" or r["status"] == "empty"]
    cards = [r for r in recs if r not in empties]
    by_repo = {r["repo"]: r for r in cards}
    errs = check_text(cards)
    if errs:
        sys.exit("BUILD FAILED, text rules:\n  " + "\n  ".join(errs))
    planned = [planned_rec(p) for p in planned_raw]
    for p in planned:
        for e in p["_edges"]:
            assert e.get("to") in by_repo or e.get("external"), "planned edge to unknown repo %s" % e.get("to")
        assert os.path.exists(os.path.join(ROOT, p["_prompt"])), "missing " + p["_prompt"]
    setup_context(cards, planned)
    live = [r for r in cards if not is_retired(r)]
    retired = [r for r in cards if is_retired(r)]
    for g in guides:
        for pk in g.get("picks", []):
            if pk["use"] not in by_repo:
                print("note: guide %s picks unknown repo %s" % (g.get("id"), pk["use"]), file=sys.stderr)
    edges = compute_edges(cards, CTX["resolve"])
    out_edges, in_edges = defaultdict(list), defaultdict(list)
    for e in edges:
        out_edges[e[0]].append(e)
        in_edges[e[1]].append(e)
    files = {}
    cap = gen_capabilities(cards, live, retired, planned, guides, gaps, by_repo)
    files.update(cap)
    for r in cards:
        pl = [(p, e) for p in planned for e in p["_edges"] if e.get("to") == r["repo"]]
        files["apps/%s.md" % r["repo"]] = build_card(r, by_repo, out_edges, in_edges, pl)
    for p in planned:
        files["apps/%s.md" % p["repo"]] = build_planned_card(p, by_repo)
    kwtext, ent = gen_keywords(live, retired, planned, gaps)
    files["KEYWORDS.md"] = kwtext
    for w in README_EXAMPLES:
        assert w in ent, "README example keyword %r is not in the keyword index" % w
    files["README.md"] = gen_readme(cards, live, retired, planned, gaps, meta, empties)
    files["MIND_MAP.md"] = gen_mindmap(live, retired, planned)
    files["CONTROL_API.md"] = gen_control(cards, live)
    files["HARDWARE.md"] = gen_hardware(live, retired, planned, guides, by_repo)
    files["MODULES.md"] = gen_modules(cards)
    files["CONNECTIONS.md"] = gen_connections(cards, planned, edges, by_repo)
    files["STATUS.md"] = gen_status(recs, cards, live, retired, empties, meta, edges)
    files["index.html"] = gen_index(live, retired, planned, guides, gaps, by_repo)
    files = {k: render(k, v) for k, v in files.items()}
    bad = check_links(files)
    if bad:
        sys.exit("BROKEN LINKS:\n  " + "\n  ".join(bad))
    bad = check_privacy(files)
    if bad:
        sys.exit("PRIVACY PATTERNS IN OUTPUT:\n  " + "\n  ".join(bad))
    summary = "cards %d (live %d, retired %d), planned %d, empty %d, edges %d, files %d" % (
        len(cards), len(live), len(retired), len(planned), len(empties), len(edges), len(files))
    return files, summary


def disk_generated():
    found = set()
    for d in ("apps", "capabilities"):
        p = os.path.join(ROOT, d)
        if os.path.isdir(p):
            found |= {"%s/%s" % (d, f) for f in os.listdir(p) if f.endswith(".md")}
    return found


def main():
    args = sys.argv[1:]
    files, summary = generate()
    if "--check" in args:
        diff = []
        for f, t in sorted(files.items()):
            p = os.path.join(ROOT, f)
            if not os.path.exists(p):
                diff.append("missing " + f)
            else:
                with open(p, encoding="utf-8", newline="") as fh:
                    if fh.read() != t:
                        diff.append("differs " + f)
        diff += ["stale " + f for f in sorted(disk_generated() - set(files))]
        if diff:
            print("generated files are out of date:\n  " + "\n  ".join(diff))
            sys.exit(1)
        print("up to date: " + summary)
        return
    for f in disk_generated() - set(files):
        os.remove(os.path.join(ROOT, f))
    for f, t in files.items():
        p = os.path.join(ROOT, f)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(t)
    print(summary + ", links ok")


if __name__ == "__main__":
    main()
