# python_template

小規模ツールをサクッと作れるリポジトリテンプレート

## 構成

- Python 3.12
- [Ruff](https://docs.astral.sh/ruff/) — Linter / Formatter / import整理
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.pylance) — 型チェック (standard)
- [pytest](https://docs.pytest.org/) — テスト
- src-layout (`src/myapp/`)

## セットアップ

### 1. テンプレートから新しいリポジトリを作成

GitHub の "Use this template" からリポジトリを作成する。

### 2. 環境構築（Windows）

```bat
setup.bat
```

venv の作成と dev 依存のインストールを一括で行う。

### 3. venv を有効化（毎回）

```bat
.venv\Scripts\activate.bat
```

### 4. VSCode で開く

```bat
code .
```

初回起動時に推奨拡張機能のインストールを促される。

### 5. パッケージ名を変更する

`src/myapp/` を `src/<your_package_name>/` にリネームし、以下を合わせて変更する。

- `pyproject.toml` の `name` と `known-first-party`
- `tests/test_main.py` の import

## よく使うコマンド

```bat
# Lint
ruff check src/ tests/

# Format
ruff format src/ tests/

# Lint + import整理（自動修正）
ruff check --fix src/ tests/

# テスト
pytest tests/ -v
```

## 環境変数

`.env.example` を `.env` にコピーして値を設定する。`.env` はgitignoreされている。
