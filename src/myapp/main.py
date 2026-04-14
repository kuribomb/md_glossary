from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path

from markdown_it import MarkdownIt


@dataclass
class Section:
    heading: str
    level: int
    title: str
    body_lines: list[str] = field(default_factory=list)
    children: list[Section] = field(default_factory=list)


def parse(text: str) -> tuple[list[str], list[Section]]:
    """Markdownテキストをパースしてセクションツリーに変換する。"""
    tokens = MarkdownIt().parse(text)
    all_lines = text.splitlines()

    # 見出しトークンから行番号・レベル・タイトルを収集
    heading_info: list[tuple[int, int, str]] = [
        (tok.map[0], int(tok.tag[1]), tokens[i + 1].content)
        for i, tok in enumerate(tokens)
        if tok.type == "heading_open" and tok.map is not None
    ]

    if not heading_info:
        return all_lines, []

    # 各見出しの body_lines を行番号範囲で切り出す
    sections_flat: list[Section] = []
    for idx, (line_no, level, title) in enumerate(heading_info):
        next_heading = heading_info[idx + 1][0] if idx + 1 < len(heading_info) else len(all_lines)
        sections_flat.append(Section(
            heading=all_lines[line_no],
            level=level,
            title=title,
            body_lines=all_lines[line_no + 1 : next_heading],
        ))

    # スタックで階層構造を構築
    root_sections: list[Section] = []
    stack: list[Section] = []
    for sec in sections_flat:
        while stack and stack[-1].level >= sec.level:
            stack.pop()
        (stack[-1].children if stack else root_sections).append(sec)
        stack.append(sec)

    return all_lines[: heading_info[0][0]], root_sections


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
