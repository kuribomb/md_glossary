from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s*(.*)")


@dataclass
class Section:
    heading: str
    level: int
    title: str
    body_lines: list[str] = field(default_factory=list)
    children: list[Section] = field(default_factory=list)


def parse(text: str) -> tuple[list[str], list[Section]]:
    """Markdownテキストをパースしてセクションツリーに変換する。"""
    root_body: list[str] = []
    sections: list[Section] = []
    stack: list[Section] = []

    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            section = Section(heading=line, level=level, title=title)
            while stack and stack[-1].level >= level:
                stack.pop()
            if stack:
                stack[-1].children.append(section)
            else:
                sections.append(section)
            stack.append(section)
        else:
            if stack:
                stack[-1].body_lines.append(line)
            else:
                root_body.append(line)

    return root_body, sections


def sort_sections(sections: list[Section]) -> list[Section]:
    """セクションを再帰的にアルファベット順でソートする。"""
    for sec in sections:
        sec.children = sort_sections(sec.children)
    return sorted(sections, key=lambda s: s.title.lower())


def render(root_body: list[str], sections: list[Section]) -> str:
    """セクションツリーをMarkdownテキストに変換する。"""
    lines: list[str] = list(root_body)

    def _render(sec: Section) -> None:
        lines.append(sec.heading)
        lines.extend(sec.body_lines)
        for child in sec.children:
            _render(child)

    for sec in sections:
        _render(sec)

    return "\n".join(lines)


def sort_markdown(text: str) -> str:
    """Markdownテキストの見出しをソートして返す。"""
    root_body, sections = parse(text)
    sections = sort_sections(sections)
    return render(root_body, sections)


def main() -> None:
    if len(sys.argv) >= 2:
        path = Path(sys.argv[1])
        text = path.read_text(encoding="utf-8")
        sorted_text = sort_markdown(text)
        if "--inplace" in sys.argv:
            path.write_text(sorted_text, encoding="utf-8")
            print(f"Sorted: {path}", file=sys.stderr)
        else:
            print(sorted_text, end="")
    else:
        text = sys.stdin.read()
        print(sort_markdown(text), end="")


if __name__ == "__main__":
    main()
