"""Render the Project Portfolio block of README.md from projects.yml.

The block between `<!-- portfolio:start -->` and `<!-- portfolio:end -->` is replaced; everything
else in README.md is left alone. Structure (fixed by the 2026-09-20 nav-fix): an index with counts,
then per section an anchored <h2 id="…">Title <sub>(N projects)</sub></h2>, a two-column table of
rows, a Return-to-Index link and a "Jump to" strip. Section IV is wrapped in <details open> (no name
attribute); no other section is collapsible and no heading ever sits inside a <summary>.

Usage: python3 scripts/update_readme.py [--check]   (--check exits 1 when README.md is stale)
"""

from __future__ import annotations

import html
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
DATA = ROOT / "projects.yml"
START, END = "<!-- portfolio:start -->", "<!-- portfolio:end -->"

SECTIONS = [
    ("I", "data-ml", "Data Architecture &amp; Machine Learning", "projects"),
    ("II", "cloud-security", "Cloud Infrastructure &amp; Security", "projects"),
    ("III", "edtech-systems", "Educational Technology Systems", "projects"),
    ("IV", "learning-resources", "Interactive Learning Resources", "resources"),
    ("V", "developer-tooling", "Developer Tooling", "projects"),
    ("VI", "executive-tools", "Executive Decision Tools", "projects"),
]
IMG = "https://images.unsplash.com/photo-{id}?auto=format&amp;fit=crop&amp;w=300&amp;h=180&amp;q=80"
GH = "https://github.com/Freddricklogan/{repo}"


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def row(p: dict) -> str:
    repo = p["repo"]
    href = p.get("live") or GH.format(repo=repo)
    label = "Format" if p.get("format") else "Tech"
    links = [f'<a href="{GH.format(repo=repo)}">Source</a>']
    if p.get("case_study"):
        links.append(f'<a href="{GH.format(repo=repo)}/blob/main/{p["case_study"]}">Case study</a>')
    if p.get("ci"):
        links.append(
            f'<a href="{GH.format(repo=repo)}/actions/workflows/deploy.yml">'
            f'<img src="{GH.format(repo=repo)}/actions/workflows/deploy.yml/badge.svg" alt="CI status for {esc(p["title"])}" height="16" /></a>'
        )
    if p.get("replaces"):
        links.append("<sub>replaces " + ", ".join(esc(r) for r in p["replaces"]) + "</sub>")
    if p.get("status") == "archived" and p.get("successor"):
        links.append(f'<sub>archived — see <a href="{GH.format(repo=p["successor"])}">{esc(p["successor"])}</a></sub>')
    return (
        "<tr>\n"
        f'<td width="150"><img src="{IMG.format(id=p["image"])}" width="150" alt="{esc(p["alt"])}" /></td>\n'
        f'<td valign="top"><b><a href="{esc(href)}">{esc(p["title"])}</a></b><br />{esc(p["description"])}'
        f'<br /><sub><b>{label}:</b> {esc(p["tech"])}</sub><br /><sub>{" &middot; ".join(links)}</sub></td>\n'
        "</tr>"
    )


def jump() -> str:
    parts = " &middot; ".join(f'<a href="#{sid}">{num}</a>' for num, sid, _, _ in SECTIONS)
    return f'<a href="#project-portfolio">&#8679; Return to Index</a><br>\n<sub>Jump to: {parts}</sub>'


def render(projects: list[dict]) -> str:
    tier = {"T1": 0, "T2": 1, "T3": 2}
    by = {
        num: sorted((p for p in projects if p["section"] == num), key=lambda p: tier.get(p.get("tier"), 9))
        for num, *_ in SECTIONS
    }
    out = [START, "", "## Project Portfolio", "", '<div align="center">', "", "**Project and Framework Index**", ""]
    out.append(
        "<br>\n".join(
            f'[{num}. {title}](#{sid}) &mdash; {len(by[num])} {noun}' for num, sid, title, noun in SECTIONS
        )
    )
    out += ["", "</div>", ""]
    for num, sid, title, noun in SECTIONS:
        items = by[num]
        out.append(f'<h2 id="{sid}">{num}. {title} <sub>({len(items)} {noun})</sub></h2>')
        out.append("")
        if num == "IV":
            out += ["<details open>", f"<summary>Show all {len(items)} resources</summary>", "<br>"]
        out.append('<table border="0">')
        out += [row(p) for p in items]
        out.append("</table>")
        out.append("<br />")
        if num == "IV":
            out.append("</details>")
        out.append(jump())
        out.append("")
    out.append(END)
    return "\n".join(out)


def main() -> int:
    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))["projects"]
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit("README.md has no portfolio markers")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + render(data) + tail
    if "--check" in sys.argv:
        if new != text:
            print("README.md is stale — run scripts/update_readme.py")
            return 1
        print("README.md is up to date")
        return 0
    README.write_text(new, encoding="utf-8")
    print(f"rendered {len(data)} entries into README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
