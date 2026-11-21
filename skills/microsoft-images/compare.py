#!/usr/bin/env python3
"""compare.py: Google picture next to Microsoft picture of the same subject.

    python3 compare.py <google_dir> <microsoft_dir> <out_dir> [--height 1080] [--title "Subject"]

A pair is two files with the same name once the maker's suffix is taken off:
    room (nano banana).png   +   room (mai image 2.7).png        -> pair "room"
    room.jpg                 +   room (mai image 2.7 flash).png  -> pair "room"
For every pair it writes <out_dir>/<name>.jpg (both at the same height, a label under each),
then sheet.jpg (all pairs under each other) and comparison.html (the same, as a page).
Files with no partner are listed and skipped. Needs ImageMagick (`convert`), nothing else.
Exit code 0 when at least one pair was made, 1 when none.
"""
import argparse, html, os, re, subprocess, sys

EXT = ('.png', '.jpg', '.jpeg', '.webp')
SUFFIX = re.compile(r'\s*\((nano banana[^)]*|gemini[^)]*|mai image[^)]*|microsoft[^)]*)\)\s*$', re.I)


def stems(folder):
    """name without maker suffix -> (file name, maker label or '')"""
    out = {}
    for f in sorted(os.listdir(folder)):
        base, ext = os.path.splitext(f)
        if ext.lower() not in EXT:
            continue
        m = SUFFIX.search(base)
        key = SUFFIX.sub('', base).strip().lower()
        out.setdefault(key, (f, m.group(1) if m else ''))
    return out


def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"{cmd[0]} failed: {r.stderr.strip()[:400]}")


def panel(src, label, height, dst):
    # the picture at one height, a dark strip with the label under it
    run('convert', src, '+repage', '-auto-orient', '-resize', f'x{height}', '-background', '#111', '-flatten',
        '(', '-background', '#111', '-fill', '#eee', '-pointsize', str(max(18, height // 30)),
        '-gravity', 'center', f'label:{label}', '-bordercolor', '#111', '-border', '0x12', ')',
        '-gravity', 'center', '-background', '#111', '-append', dst)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('google_dir'); ap.add_argument('microsoft_dir'); ap.add_argument('out_dir')
    ap.add_argument('--height', type=int, default=1080)
    ap.add_argument('--title', default='Google and Microsoft, the same subject')
    a = ap.parse_args()
    g, m = stems(a.google_dir), stems(a.microsoft_dir)
    pairs = sorted(set(g) & set(m))
    for k in sorted(set(g) - set(m)): print(f'no Microsoft picture for: {g[k][0]}')
    for k in sorted(set(m) - set(g)): print(f'no Google picture for: {m[k][0]}')
    if not pairs:
        print('no pairs: nothing written'); sys.exit(1)
    os.makedirs(a.out_dir, exist_ok=True)
    made = []
    for k in pairs:
        gl = 'Google: ' + (g[k][1] or 'Nano Banana (Gemini)')
        ml = 'Microsoft: ' + (m[k][1] or 'MAI Image 2.7')
        left, right = os.path.join(a.out_dir, f'.{k}.g.png'), os.path.join(a.out_dir, f'.{k}.m.png')
        panel(os.path.join(a.google_dir, g[k][0]), gl, a.height, left)
        panel(os.path.join(a.microsoft_dir, m[k][0]), ml, a.height, right)
        dst = os.path.join(a.out_dir, f'{k}.jpg')
        run('convert', left, right, '-background', '#111', '-gravity', 'north', '+smush', '16',
            '-bordercolor', '#111', '-border', '16', '-quality', '90', dst)
        os.remove(left); os.remove(right)
        made.append((k, dst, gl, ml)); print(f'pair: {dst}')
    sheet = os.path.join(a.out_dir, 'sheet.jpg')
    run('convert', *[d for _, d, _, _ in made], '-background', '#111', '-gravity', 'center', '-append',
        '-resize', '2400x>', '-quality', '88', sheet)
    rows = '\n'.join(
        f'<section><h2>{html.escape(k)}</h2><img src="{html.escape(os.path.basename(d))}" alt="{html.escape(gl)} | {html.escape(ml)}"></section>'
        for k, d, gl, ml in made)
    with open(os.path.join(a.out_dir, 'comparison.html'), 'w', encoding='utf-8') as fh:
        fh.write('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                 f'<title>{html.escape(a.title)}</title>'
                 '<style>body{background:#111;color:#eee;font:16px system-ui;margin:0;padding:16px}'
                 'img{max-width:100%;height:auto;display:block}h1{font-size:22px}h2{font-size:16px;margin:24px 0 8px}</style>'
                 f'<h1>{html.escape(a.title)}</h1><p>Left: Google. Right: Microsoft. Same prompt, same aspect ratio.</p>\n{rows}\n')
    print(f'{len(made)} pair(s); sheet: {sheet}; page: {os.path.join(a.out_dir, "comparison.html")}')


if __name__ == '__main__':
    main()
