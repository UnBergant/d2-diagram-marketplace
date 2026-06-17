#!/usr/bin/env python3
"""Splice an EXACT rendered ASCII diagram into a Markdown file.

Replaces the content of the first ```-fenced code block that appears AFTER a
given marker line with the exact contents of <render.txt>. Use this instead of
hand-retyping/trimming a rendered diagram into docs (trimming drops lines/arrows
and misaligns).

Usage:
  python splice-ascii.py <doc.md> <render.txt> "<marker line text>"
"""
import sys

def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    md_path, txt_path, marker = sys.argv[1], sys.argv[2], sys.argv[3]
    ascii_content = open(txt_path, encoding="utf-8").read().rstrip("\n")
    md = open(md_path, encoding="utf-8").read()

    mi = md.find(marker)
    if mi < 0:
        print(f"ERROR: marker not found: {marker!r}")
        sys.exit(2)
    fence_open = md.find("```", mi)
    if fence_open < 0:
        print("ERROR: no opening ``` after marker")
        sys.exit(2)
    body_start = md.find("\n", fence_open) + 1          # after ```\n
    fence_close = md.find("\n```", body_start)
    if fence_close < 0:
        print("ERROR: no closing ``` fence")
        sys.exit(2)

    new_md = md[:body_start] + ascii_content + md[fence_close:]
    open(md_path, "w", encoding="utf-8", newline="\n").write(new_md)
    print(f"OK: spliced {ascii_content.count(chr(10)) + 1} lines into {md_path}")

if __name__ == "__main__":
    main()
