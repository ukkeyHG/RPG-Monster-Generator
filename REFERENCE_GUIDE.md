# RPG Monster Generator 設定リファレンス

このガイドでは、`RPG Monster Generator` ノードで選択可能な各項目の意味と、生成される画像への影響について解説します。

---

## 1. Style (画風・技法)
画像全体の描き方を決定します。

| スタイル名 | 概要 | 推奨設定 (自動出力) |
| :--- | :--- | :--- |
| **Oil Painting** | 重厚な油彩画 | Steps: 30, CFG: 8.0, Sampler: dpmpp_2m |
| **Cinematic Realistic** | 写実的なリアル | Steps: 35, CFG: 6.5, Sampler: dpmpp_3m_sde_gpu |
| **Ancient Sketch** | 手書きスケッチ | Steps: 20, CFG: 5.0, Sampler: euler |

---

## 7. KSampler との連携方法
このノードは、選択したスタイルに最適な KSampler の設定値（steps, cfg, sampler_name, scheduler）を自動的に出力します。

### 設定手順
1.  **KSampler ノードを用意する**: 通常の `KSampler` ノードを配置します。
2.  **入力をピンに変換する**: `KSampler` ノードの上で **右クリック** し、以下を選択して各項目を入力ピンに変換します：
    - `convert steps to input`
    - `convert cfg to input`
    - `convert sampler_name to input`
    - `convert scheduler to input`
3.  **線を繋ぐ**: `RPG Monster Generator` ノードの各出力ピンから、`KSampler` の対応する入力ピンへ線を繋ぎます。

これで、`style` を切り替えるだけで、プロンプトだけでなく生成設定も自動的に最適化されるようになります。

## 2. Species (種族)
モンスターの基本的な外見を決定します。

- **Slime**: 半透明、粘液質、核が見える。
- **Skeleton**: 露出した骨、暗い眼窩、崩れかけた質感。
- **Demon**: 角、翼、筋肉質な体、威圧感。
- **Dragon**: 鱗、巨大な体、鋭い爪、爬虫類的な瞳。
- **Spider**: 八本の脚、複数の目、毛深い体質。
- **Mimic**: 宝箱に擬態した怪物、鋭い牙、長い舌。
- **Gargoyle**: 石造りの翼を持つ怪物、ひび割れた石の肌。
- **Golem**: 岩や魔法の構築物、重厚な体躯。
- **Frog**: 湿った肌、大きな口、突き出た目。

---

## 3. Element (属性)
モンスターが纏うエネルギーや視覚的なエフェクトを決定します。

- **None**: 属性なし。
- **Fire**: 炎の粒子、煙、赤やオレンジの輝き。
- **Ice**: 氷の結晶、冷気、青白く澄んだ輝き。
- **Poison**: 紫や緑の霧、毒々しい泡、腐食感。
- **Lightning**: 電気の放電、白い閃光、弾ける火花。
- **Dark**: 黒い影のオーラ、光を吸収する虚無感。

---

## 4. Variant (変異・個体差)
モンスターの「状態」や「個体としての特徴」を決定します。

- **Normal**: 標準的な個体。
- **Enraged**: 怒り狂った状態。血管の隆起や攻撃的なポーズ。
- **Ancient**: 長い年月を経た個体。体毛や岩肌に苔が生え、風化している。
- **Mutated**: 突然変異。不規則な結晶や棘が体から生えている。

> [!TIP]
> **「Style: Ancient Sketch」と「Variant: Ancient」の違い**
> - **Style: Ancient Sketch** は「古いスケッチという**描き方**」です。
> - **Variant: Ancient** は「モンスターが**長生きしている**」という設定です。
> 両方を組み合わせると、「古文書に記された古の化け物」という非常に雰囲気のある画像になります。

---

## 5. Rank (強さ・希少度)
モンスターの迫力や装飾の豪華さを決定します。

- **Common**: 一般的な個体。
- **Elite**: 少し強力な個体。装飾や体躯が際立つ。
- **Boss**: 強大で威厳のある個体。画面を支配する存在感。

---

## 6. Scene (背景・場所)
モンスターが出現する場所（背景）を決定します。

- **Dungeon**: 暗い石造りの地下牢。
- **Lava Cave**: 溶岩が流れる灼熱の洞窟。
- **Ice Vault**: 氷に閉ざされた古代の宝物庫。
- **Graveyard**: 地下の墓地、カタコンベ。
- **Throne Room**: 廃墟となった玉座の間。

---

## 組み合わせのコツ
- **リアルにしたい**: `Cinematic Realistic` を選び、KSampler の CFG を少し下げてください。
- **研究資料風**: `Ancient Sketch` と `Scene: Graveyard` や `Variant: Ancient` を組み合わせるのがおすすめです。
- **属性の視認性を高める**: `Element: Fire` や `Lightning` を選んだ際は、少し暗い `Scene` を選ぶと光が映えます。
