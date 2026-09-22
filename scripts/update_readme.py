"""Render the Project Portfolio block of README.md from projects.yml and the copy file.

The block between `<!-- portfolio:start -->` and `<!-- portfolio:end -->` is replaced; everything
else in README.md is left alone. It contains, in order: the Featured grid and the five-minute review
(verbatim HTML from docs/copy/profile-readme-copy.md with `{{repo.thumbnail}}` / `{{repo.demo}}`
resolved from projects.yml), the index with counts, one anchored section per `sections:` entry
(rows sorted by tier; a 12 px swatch in the repo's category palette before each title; `collapsible`
sections wrapped in <details open>; no heading inside a <summary>), and the Roadmap.

Usage: python3 scripts/update_readme.py [--check]   (--check exits 1 when README.md is stale)
"""

from __future__ import annotations

import re
import sys
from html import escape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DATA = ROOT / "projects.yml"
COPY = ROOT / "docs" / "copy" / "profile-readme-copy.md"
BLUEPRINT = "docs/MODERNIZATION_BLUEPRINT.md"
START, END = "<!-- portfolio:start -->", "<!-- portfolio:end -->"

IMG = "https://images.unsplash.com/photo-{id}?auto=format&amp;fit=crop&amp;w=300&amp;h=180&amp;q=80"
GH = "https://github.com/Freddricklogan/{repo}"
TIER = {"T1": ("Flagship", "58a6ff"), "T2": ("Showcase", "3fb950"), "T3": ("Consolidated", "8b98b0")}
# Category palettes (dark-scheme primary / secondary), the same values as the Executive Shell's exec-shell.css.
THEME_HUES = {
    "signal": ("818cf8", "2dd4bf"), "graphite": ("f59e0b", "a3e635"), "ember": ("e0b356", "f4845f"),
    "plum": ("c084fc", "6ee7b7"), "forest": ("a3e635", "7dd3fc"), "midnight": ("d4a95a", "58a6ff"),
}
README_DEMO_SECTION = "#6-live-demo--production-showcase"


def gh(repo: str) -> str:
    return GH.format(repo=repo)


def thumbnail(p: dict) -> str:
    return IMG.format(id=p["image"])


def demo(p: dict) -> str:
    """The live URL, or the README's §6 (deploy-in-one-click + demo credentials) when none is live."""
    return p["live"] or f"{gh(p['repo'])}{README_DEMO_SECTION}"


def demo_note(p: dict) -> str:
    if p["live"]:
        return ""
    route = p.get("demo_route", "/")
    return (
        f'<br /><sub><i>Not yet deployed — the link opens the README section with the one-click deploy and the '
        f"demo credentials; once launched the explorer is the Scalar reference at <code>{escape(route)}</code>.</i></sub>"
    )


def copy_blocks(text: str) -> dict[str, str]:
    """The copy file's ```html fences keyed by their preceding H2, plus the two quoted intro lines."""
    blocks: dict[str, str] = {}
    for heading, body in re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        fence = re.search(r"```html\n(.*?)```", body, re.S)
        quote = re.search(r"^> (.+)$", body, re.M)
        if fence:
            blocks[heading.strip()] = fence.group(1).strip()
        elif quote:
            blocks[heading.strip()] = quote.group(1).strip()
    return blocks


def resolve(html: str, by: dict[str, dict]) -> str:
    """Fill {{repo.thumbnail}} / {{repo.demo}}; a repo with no live demo also gets a note after its links."""
    def sub(m: re.Match[str]) -> str:
        p = by[m.group(1)]
        return thumbnail(p) if m.group(2) == "thumbnail" else demo(p)

    out = re.sub(r"\{\{([a-z0-9-]+)\.(thumbnail|demo)\}\}", sub, html)
    for repo, p in by.items():
        if p["live"] or demo(p) not in out:
            continue
        if f'href="{gh(repo)}">Source</a>' in out:  # a Featured cell: full note after its links
            out = out.replace(f'href="{gh(repo)}">Source</a>', f'href="{gh(repo)}">Source</a>{demo_note(p)}', 1)
        else:  # prose: a short flag after the demo link
            out = re.sub(rf'(<a href="{re.escape(demo(p))}">(?:(?!</a>).)*</a>)', r"\1 <sub>(not yet deployed; the link opens the README section with the deploy and demo credentials)</sub>", out, count=1)
    return out


def swatch(p: dict) -> str:
    """12 px square in the repo's category colour (its accent when it uses the secondary hue)."""
    primary, secondary = THEME_HUES[p["theme"]]
    hue = secondary if p.get("accent") == "secondary" else primary
    return (
        f'<img src="https://img.shields.io/badge/%20-%20-{hue}" width="12" height="12" '
        f'alt="{escape(p["theme"])} palette" title="{escape(p["theme"])} palette" /> '
    )


def shields(p: dict) -> str:
    label, colour = TIER[p["tier"]]
    parts = [f'<img src="https://img.shields.io/badge/tier-{label}-{colour}" alt="Tier: {label}" height="16" />']
    if p.get("ci"):
        parts.append(
            f'<a href="{gh(p["repo"])}/actions/workflows/deploy.yml">'
            f'<img src="{gh(p["repo"])}/actions/workflows/deploy.yml/badge.svg" alt="CI status for {escape(p["title"])}" height="16" /></a>'
        )
    return " ".join(parts)


def row(p: dict) -> str:
    repo = p["repo"]
    href = p.get("live") or gh(repo)
    label = "Format" if p.get("format") else "Tech"
    lines = [f"<b>{label}:</b> {escape(p['tech'])}"]
    if p.get("programme"):
        lines.append(f"<b>Programme:</b> {escape(p['programme'])} (issued {escape(p['issued'])})")
    links = [f'<a href="{gh(repo)}">Source</a>']
    if p.get("case_study"):
        links.append(f'<a href="{gh(repo)}/blob/main/{p["case_study"]}">Case study</a>')
    if p.get("replaces"):
        links.append("replaces " + ", ".join(escape(r) for r in p["replaces"]))
    if p.get("status") == "archived" and p.get("successor"):
        links.append(f'archived — see <a href="{gh(p["successor"])}">{escape(p["successor"])}</a>')
    subs = "".join(f"<br /><sub>{line}</sub>" for line in lines)
    return (
        "<tr>\n"
        f'<td width="150"><img src="{thumbnail(p)}" width="150" alt="{escape(p["alt"])}" /></td>\n'
        f'<td valign="top">{swatch(p)}<b><a href="{escape(href)}">{escape(p["title"])}</a></b><br />{escape(p["description"])}'
        f'{subs}<br /><sub>{" &middot; ".join(links)}</sub><br />{shields(p)}</td>\n'
        "</tr>"
    )


def render(data: dict, copy: dict[str, str]) -> str:
    sections = data["sections"]
    by = {p["repo"]: p for p in data["projects"]}
    tier_order = {"T1": 0, "T2": 1, "T3": 2}
    grouped = {
        s["num"]: sorted((p for p in data["projects"] if p["section"] == s["num"]), key=lambda p: tier_order[p["tier"]])
        for s in sections
    }
    jump = '<a href="#project-portfolio">&#8679; Return to Index</a><br>\n<sub>Jump to: ' + " &middot; ".join(
        f'<a href="#{s["id"]}">{s["num"]}</a>' for s in sections
    ) + "</sub>"

    out = [START, "", resolve(copy["Featured (3 × 2 grid, above the fold)"], by), "", resolve(copy["Review this portfolio in five minutes"], by), ""]
    out += ["## Project Portfolio", "", '<div align="center">', "", "**Project and Framework Index**", ""]
    out.append("<br>\n".join(f'[{s["num"]}. {s["title"]}](#{s["id"]}) &mdash; {len(grouped[s["num"]])} {s["noun"]}' for s in sections))
    out += ["", "</div>", ""]
    for s in sections:
        items = grouped[s["num"]]
        out += [f'<h2 id="{s["id"]}">{s["num"]}. {s["title"]} <sub>({len(items)} {s["noun"]})</sub></h2>', ""]
        if s.get("intro"):
            out += [f"<p>{copy[s['intro'].removeprefix('copy:')] if s['intro'].startswith('copy:') else s['intro']}</p>", ""]
        if s.get("collapsible"):
            out += ["<details open>", f"<summary>Show all {len(items)} {s['noun']}</summary>", "<br>"]
        out += ['<table border="0">', *(row(p) for p in items), "</table>", "<br />"]
        if s.get("collapsible"):
            out.append("</details>")
        out += [jump, ""]
    out += ['<h2 id="roadmap">Roadmap</h2>', "", f"<p>{copy['Roadmap intro line']}</p>", "", "<ul>"]
    out += [f'<li><b><a href="{BLUEPRINT}#{r["anchor"]}">{escape(r["name"])}</a></b> &mdash; {escape(r["pitch"])}</li>' for r in data["roadmap"]]
    out += ["</ul>", "", END]
    return "\n".join(out)


def main() -> int:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    copy = copy_blocks(COPY.read_text(encoding="utf-8"))
    copy["section-vi"] = copy["Section VI intro line"]
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit("README.md has no portfolio markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + render(data, copy) + tail
    if "--check" in sys.argv:
        if new != text:
            print("README.md is stale — run scripts/update_readme.py")
            return 1
        print("README.md is up to date")
        return 0
    README.write_text(new, encoding="utf-8")
    print(f"rendered {len(data['projects'])} entries, {len(data['featured'])} featured, {len(data['roadmap'])} roadmap items into README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
