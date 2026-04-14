# このリポジトリについて

Python プロジェクト用テンプレートリポジトリ。

## ブランチ構成

```
main              ← インデックス（README.md のみ。ブランチ一覧・使い方を記載）
python-base       ← 共通ベーステンプレート
python/fastapi    ← python-base から派生（FastAPI）
python/svelte     ← python-base から派生（FastAPI + SvelteKit）
python/pyside6    ← python-base から派生（PySide6）
```

## ブランチ変更時のルール

### python-base を変更した場合

`python-base` に変更を加えた場合は、**すべての `python/*` ブランチにも同じ変更を適用すること。**

対象ブランチ:
- `python/fastapi`
- `python/svelte`
- `python/pyside6`

### main の README.md を常に最新に保つ

`main` ブランチの `README.md` はリポジトリのインデックスとして機能する。
ブランチの追加・削除・内容変更が生じた場合は、**必ず `main` の `README.md` を更新すること。**

更新が必要なケース:
- 新しいテンプレートブランチを追加したとき
- テンプレートブランチを削除したとき
- ブランチの用途・技術スタックが変わったとき
