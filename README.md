# RPG Monster Generator

Echoes of Eltnia (エルトニアの残響) で使用するモンスター画像を生成するための ComfyUI カスタムノードです。

## 概要

このツールは、ゲームの世界観に合わせた「重厚な油彩画スタイル」のモンスター画像を生成するためのプロンプトを自動構成します。
種族、属性、バリエーション、ランク、シーンを選択することで、最適なポジティブ/ネガティブプロンプトを出力します。

## 構成

- `RPG-Monster-Generator.py`: ComfyUI 用のカスタムノード本体。

- `rpg_character_data/`: 種族や属性などの定義データ。

## 導入方法

1.  ComfyUI の `custom_nodes` ディレクトリに移動します。
2.  このリポジトリをクローンするか、ファイルを配置します。
    ```bash
    git clone https://github.com/ukkeyHG/RPG-Monster-Generator.git
    ```
3.  ComfyUI を再起動すると、`RPG` カテゴリに `RPG Generator` ノードが追加されます。

## 開発について

このリポジトリは `Echoes-of-Eltnia` プロジェクトと連携して開発されています。
データ構造の変更は、両方のプロジェクトの整合性を保つように注意してください。
