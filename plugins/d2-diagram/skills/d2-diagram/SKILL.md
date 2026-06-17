---
name: d2-diagram
description: "Generate clean, auto-laid-out diagrams with D2 (diagram-as-code). Renders to SVG/PNG (docs) AND exact ASCII (terminal). Use for flowcharts, architecture, branch/release/CI-CD diagrams, or any boxes-and-arrows diagram — replaces hand-drawn ASCII."
user-invocable: true
allowed-tools: "Bash, Read, Write, Edit"
---

# D2 Diagram Generator

## Purpose
Draw diagrams as **code** with D2 so the engine does the layout — never hand-align boxes,
never hand-draw cyclic graphs. One `.d2` source renders to a crisp **SVG/PNG** (for docs/Wiki)
and to **exact ASCII** (for terminals / `.md` code blocks).

## Prerequisite
D2 is installed at `C:\Program Files\D2\d2.exe` (winget `Terrastruct.D2`). In Bash use:
`D2="/c/Program Files/D2/d2.exe"`. If missing: `winget install --id Terrastruct.D2 -e --silent`.

## Workflow
1. Write the diagram as a `.d2` file (see Conventions).
2. Render per target:
   - **Image (docs):**  `"$D2" file.d2 file.svg`   (or `file.png`)
   - **ASCII (terminal):** `"$D2" --ascii-mode extended file.d2 file.txt`  (`standard` = pure ASCII)
3. Show the user: paste the `.txt` for terminal, send the `.svg`/`.png` as a file.
4. **To embed ASCII in a Markdown doc, splice the EXACT rendered `.txt`** — do not retype it
   (see Anti-patterns). Use the helper:
   `python "${CLAUDE_SKILL_DIR}/splice-ascii.py" <doc.md> <render.txt> "<marker line in the md>"`
   It replaces the first ```` ``` ```` fenced block after the marker line with the file's content.

## Conventions (what made diagrams read well)
- **Two layouts, one model:** vertical `direction: down` reads best as **terminal ASCII**;
  wide `direction: right` lays out more **balanced for the image**. Keep both `.d2` files.
- **Distinct node types** so categories don't blur: e.g. git branches = rounded/stadium
  (`master([master])` in mmd, or default rounded box in D2), environments = `shape: cylinder`.
- **Color via `classes:`** (only affects SVG/PNG, harmless in ASCII):
  ```d2
  classes: {
    branch: { style: { border-radius: 10; fill: "#eaf2ff"; stroke: "#1a56db" } }
    env:    { shape: cylinder; style: { fill: "#e9f7ef"; stroke: "#1e7e44" } }
  }
  node.class: branch
  ```
- **Emphasize the key edge** (e.g. the promote/merge-back): `{ style.stroke: "#188038"; style.stroke-width: 3 }`.
- **Secondary edges recede:** deploy/async edges `{ style.stroke-dash: 4; style.stroke: "#9aa0a6" }`.
- Group with containers (`branches: Git branches { ... }`) for the image; note containers can
  force long cross-edges in ASCII — drop them or switch to `direction: right` if it looks lopsided.

## ASCII gotchas
- **Single-line labels only.** `\n` / multi-line labels corrupt the ASCII render (boxes break).
  Put descriptions in surrounding prose, not inside nodes.
- Cylinders look noisy in ASCII; use rectangles for envs if the text version must be clean.
- Titles/labels with box-drawing glyphs are fine in D2 (unlike the old validator).

## Anti-patterns
- **NEVER hand-retype or trim the rendered ASCII into a doc.** Trimming silently drops lines and
  arrows (e.g. a merge-back arrow) and misaligns — splice the exact `.txt` instead.
- Don't hand-align ASCII at all — if a layout is wrong, change the `.d2`, not the output.
- Don't rely on Mermaid for terminal output (it has none) or for Azure DevOps Repos `.md` (renders
  only in the Wiki). D2 gives both ASCII and a committed SVG.

## Commit for docs
Commit the `.d2` source(s) + rendered `.svg` (and `.txt`) so the diagram is regenerable and
reviewable in PRs. Reference the image with `![alt](path/to/file.svg)`.
