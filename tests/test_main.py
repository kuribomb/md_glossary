import pytest

from myapp.main import sort_markdown


def test_basic_sort() -> None:
    """ユーザーサンプルのケース: H1とH2を含む構造のソート"""
    text = "# B\n## No3\n##No1\n# A\n## No2\n## No4"
    expected = "# A\n## No2\n## No4\n# B\n##No1\n## No3"
    assert sort_markdown(text) == expected


def test_preserves_body_lines() -> None:
    """見出し直下のテキスト行が保持されること"""
    text = "# B\nBの説明\n# A\nAの説明"
    expected = "# A\nAの説明\n# B\nBの説明"
    assert sort_markdown(text) == expected


def test_root_body_preserved() -> None:
    """最初の見出しより前の行が保持されること"""
    text = "前置きテキスト\n\n# B\n# A"
    expected = "前置きテキスト\n\n# A\n# B"
    assert sort_markdown(text) == expected


def test_case_insensitive_sort() -> None:
    """大文字小文字を区別せずにソートされること"""
    text = "# b\n# A\n# C"
    expected = "# A\n# b\n# C"
    assert sort_markdown(text) == expected


def test_already_sorted() -> None:
    """すでにソート済みの場合は変化しないこと"""
    text = "# A\n## No1\n## No2\n# B\n## No3"
    assert sort_markdown(text) == text


def test_single_section() -> None:
    """セクションが1つの場合は変化しないこと"""
    text = "# Only\nsome content"
    assert sort_markdown(text) == text


def test_empty_string() -> None:
    """空文字列の場合はそのまま返すこと"""
    assert sort_markdown("") == ""


def test_no_headings() -> None:
    """見出しがない場合はそのまま返すこと"""
    text = "単なるテキスト\nもう一行"
    assert sort_markdown(text) == text
