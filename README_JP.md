# md-glossary

Markdown のセクション見出しを階層構造とコンテンツを保ったままアルファベット順にソートします。

## 特徴

- 任意のネストレベルで見出しをアルファベット順（大文字・小文字を区別しない）にソート
- 各見出し直下の本文テキストをすべて保持
- 最初の見出しより前の前置きテキストを保持
- `--min-level` オプションで指定した深さ以下の見出しのみソート可能
- Python ライブラリおよび CLI ツールとして利用可能

## インストール

```bash
pip install md-glossary
```

## 使い方

### CLI

```bash
# ソート結果を標準出力に表示
md-glossary glossary.md

# ファイルを上書き保存
md-glossary --inplace glossary.md

# H3 以下のみソート（H1/H2 はそのまま）
md-glossary --min-level 3 glossary.md

# 標準入力から読み込む
cat glossary.md | md-glossary
```

### Python API

```python
from md_glossary import sort_markdown

text = """
# Zebra
大型の縞模様の動物。

# Apple
果物。

# Mango
熱帯の果物。
"""

print(sort_markdown(text))
# # Apple
# 果物。
#
# # Mango
# 熱帯の果物。
#
# # Zebra
# 大型の縞模様の動物。
```

#### 低レベル API

```python
from md_glossary import parse, sort_sections, render

root_body, sections = parse(text)
sections = sort_sections(sections, min_level=2)  # H2 以下のみソート
result = render(root_body, sections)
```

## オプション

| オプション | デフォルト | 説明 |
|---|---|---|
| `file` | 標準入力 | 入力 Markdown ファイル |
| `--inplace` | オフ | ファイルを上書き保存 |
| `--min-level N` | `1` | レベル N 以上の見出しのみソート |

## 開発

[uv](https://docs.astral.sh/uv/) が必要です。

```bash
git clone https://github.com/kuribomb/md_glossary
cd md_glossary
uv sync          # .venv を作成し、依存パッケージをインストール
```

```bash
uv run ruff check src/ tests/       # lint
uv run ruff format src/ tests/      # フォーマット
uv run pytest tests/ -v             # テスト
uv build                            # wheel + sdist をビルド
```

## 要件

- Python 3.12+
- [markdown-it-py](https://github.com/executablebooks/markdown-it-py) >= 3.0

## ライセンス

MIT
