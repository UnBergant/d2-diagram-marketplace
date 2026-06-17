# bergant-skills — Claude Code plugin marketplace

A small personal marketplace of Claude Code plugins by Igor Bergant.

## Plugins

### `d2-diagram`
Generate clean, auto-laid-out diagrams with [D2](https://d2lang.com) (diagram-as-code).
One `.d2` source renders to a crisp **SVG/PNG** (for docs/Wiki) and to **exact ASCII**
(for terminals / Markdown code blocks). Never hand-align boxes again. Includes a
`splice-ascii.py` helper that injects the exact rendered ASCII into a Markdown file
(so you never retype/trim a diagram and silently drop arrows).

Prerequisite: D2 installed — `winget install --id Terrastruct.D2 -e` (or see d2lang.com).

## Install

```text
/plugin marketplace add UnBergant/d2-diagram-marketplace
/plugin install d2-diagram@bergant-skills
```

Then invoke with `/d2-diagram` or just ask for a diagram.

To update later: `/plugin marketplace update bergant-skills`.
