---
paths: ["**/*.ts", "**/*.tsx"]
---

# TypeScript ルール

- `any` 禁止。型が不明なら `unknown` を使ってナローイング
- `interface` ではなく `type` を優先(union と整合)
- インポートは絶対パス(`@/...`)を優先
- `console.log` は本番コードに残さない
- 非同期関数は必ず `async/await`。生 Promise チェーンは避ける
