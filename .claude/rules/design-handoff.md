---
paths: ["design/handoff/**", "design/prototypes/**"]
---

# Design Handoff ルール

Claude Design から流れてきた HTML/CSS/JS を扱う時の規約。

## 大原則

- ハンドオフ生成物は **プロトタイプ扱い**。本番コードに直接マージしない
- 採用が決まったら、`projects/<name>/` 側で既存のトークン・コンポーネントに置き換えて再実装

## チェックポイント

ハンドオフを受け取ったら以下を確認:

- [ ] カラーがブランド `colors.md` のトークンと一致しているか
- [ ] フォントが `typography.md` のスケールに沿っているか
- [ ] `prefers-reduced-motion` への対応があるか
- [ ] ダークモード切り替えが必要なら `CSS variables` で対応しているか
- [ ] アクセシビリティ(コントラスト比、aria 属性、キーボード操作)
- [ ] インライン CSS が肥大していないか(本実装では分離)

## 編集時の制約

- `design/handoff/<bundle>/` 配下は **改変しない**(原本として保存)
- 派生作業は `design/prototypes/` または `projects/<name>/` で
- `notes.md` には変更経緯ではなく「このハンドオフの目的・コンテキスト」のみ書く

## アンチパターン

- ハンドオフ HTML をそのまま `projects/<name>/public/` に置く → 不可
- ハンドオフの inline style をコピペで本実装に → 不可。トークンに置き換える
- bundle.zip を解凍した中身だけコミット → 不可。zip も残す(URL 失効対策)
