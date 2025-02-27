# PDF Image Remover & Compressor 🔖✂️

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

PDFファイルから画像を完全削除しつつテキスト構造を保持するPythonツール。機密画像の除去やファイル軽量化に最適です。

## 🚀 特徴
- **画像完全削除** - XObjectを検出しNullObjectで置換
- **スマート圧縮** - pikepdfによるストリーム最適化
- **メタデータ保持** - テキスト検索可能な状態を維持
- **バッチ処理対応** - フォルダ単位での一括処理
- **ハイブリッド処理** - PyPDF2とpikepdfの併用

## ⚙️ 動作環境
- Python 3.8+
- 依存パッケージ:
  ```bash
  PyPDF2==3.0.0
  pikepdf==8.2.0

# インストール
```bash
git clone https://github.com/yourusername/pdf-image-remover.git
cd pdf-image-remover
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
# 使用方法
## 基本コマンド
```bash
python pdf_image_remover.py 入力ファイル.pdf 出力ファイル.pdf
```
# 実用例
```bash
# 単一ファイル処理
python pdf_image_remover.py document.pdf compressed_document.pdf

# フォルダ一括処理（bash/zsh）
for file in ./documents/*.pdf; do
  python pdf_image_remover.py "$file" "./output/compressed_${file##*/}"
done
```
# 技術的詳細
```mermaid
graph TD
    A[入力PDF] --> B[画像オブジェクト検出]
    B --> C[NullObject置換]
    C --> D[ストリーム圧縮]
    D --> E[最適化PDF出力]
```

⚠️ 注意事項
- レイアウト崩れが発生する可能性（特に複雑なテーブルを含むPDF）
- 対応できないケース:
  - 暗号化されたPDF
  - 画像がテキストとして埋め込まれている場合
  - 透明効果を使用した図形
- 重要なファイルは必ずバックアップを取ってから実行

❓ FAQ
Q: 画像以外の要素は削除されますか？
A: テキスト、ベクター図形、注釈などは保持されます

Q: 処理時間の目安は？
A: 平均的な文書（10ページ程度）で約2-5秒

Q: 元のPDFに戻せますか？
A: 本ツールは非破壊処理ではありません。必ず元ファイルを保持してください
