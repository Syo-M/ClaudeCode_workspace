---
paths: ["**/*.py"]
---

# Python ルール

- 型ヒントを必須(`def foo(x: int) -> str:`)
- フォーマッタは `ruff format`、リンタは `ruff check`
- `print` ではなく `logging` を使う(デバッグ用の暫定除く)
- 例外は具体クラスを catch。`except Exception:` は禁止
- パスは `pathlib.Path` を使い、文字列連結しない
