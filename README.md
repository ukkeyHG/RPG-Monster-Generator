# RPG Monster Generator

RPG用のモンスター画像を生成するための ComfyUI カスタムノードです。

## 概要

このツールは、クラシックなダークファンタジーの世界観にマッチする「重厚な油彩画スタイル」のモンスター画像を生成するためのプロンプトを自動構成します。
種族、属性、バリエーション、ランク、シーンを選択することで、最適なポジティブ/ネガティブプロンプトを出力します。

## 構成

- `rpg_monster_generator.py`: ComfyUI 用のカスタムノード本体。
- `REFERENCE_GUIDE.md`: 各設定項目（種族、属性、スタイル等）の詳細解説。
- `rpg_character_data/`: 種族や属性などの定義データ。

## 導入方法

1.  ComfyUI の `custom_nodes` ディレクトリに移動します。
2.  このリポジトリをクローンするか、ファイルを配置します。
    ```bash
    git clone https://github.com/ukkeyHG/RPG-Monster-Generator.git
    ```
3.  ComfyUI を再起動すると、`RPG` カテゴリに `RPG Generator` ノードが追加されます。
