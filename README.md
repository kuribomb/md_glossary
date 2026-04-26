# md-glossary

Alphabetically sort Markdown section headings while preserving hierarchy and content.

## Features

- Sorts headings alphabetically (case-insensitive) at any nesting level
- Preserves all body text beneath each heading
- Preserves preamble text before the first heading
- `--min-level` option to sort only headings at a specified depth and below
- Works as both a Python library and a CLI tool

## Installation

```bash
pip install md-glossary
```

## Usage

### CLI

```bash
# Print sorted output to stdout
md-glossary glossary.md

# Sort in place
md-glossary --inplace glossary.md

# Sort only H3 and deeper (leave H1/H2 untouched)
md-glossary --min-level 3 glossary.md

# Read from stdin
cat glossary.md | md-glossary
```

### Python API

```python
from md_glossary import sort_markdown

text = """
# Zebra
A large striped animal.

# Apple
A fruit.

# Mango
A tropical fruit.
"""

print(sort_markdown(text))
# # Apple
# A fruit.
#
# # Mango
# A tropical fruit.
#
# # Zebra
# A large striped animal.
```

#### Lower-level API

```python
from md_glossary import parse, sort_sections, render

root_body, sections = parse(text)
sections = sort_sections(sections, min_level=2)  # sort H2 and below only
result = render(root_body, sections)
```

## Options

| Option | Default | Description |
|---|---|---|
| `file` | stdin | Input Markdown file |
| `--inplace` | off | Overwrite file in place |
| `--min-level N` | `1` | Sort only headings at level N and deeper |

## Requirements

- Python 3.12+
- [markdown-it-py](https://github.com/executablebooks/markdown-it-py) >= 3.0

## License

MIT
