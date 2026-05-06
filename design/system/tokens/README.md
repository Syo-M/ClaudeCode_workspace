# Design Tokens(JSON)

将来 Style Dictionary 等でビルドする想定の JSON 形式トークン置き場。今は空でも OK。

## 想定フォーマット(W3C Design Tokens 準拠)

```json
{
  "color": {
    "primary": {
      "500": { "$value": "#000000", "$type": "color" }
    }
  },
  "size": {
    "spacing": {
      "md": { "$value": "16px", "$type": "dimension" }
    }
  }
}
```

## 使い分け

- **Markdown のトークン表**(`colors.md` 等) — 人間と Claude Design 向け
- **JSON のトークン**(ここ) — ビルドツール向け

両者を一致させる仕組みは将来検討。
