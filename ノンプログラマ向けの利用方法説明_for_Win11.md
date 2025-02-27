# PDFから画像を削除して圧縮するツールのご案内（Windows 11向け）
このガイドは、プログラムの知識がなくても、指定されたPythonスクリプトを使ってPDFファイルから画像を削除し、ファイルサイズを小さくする方法をWindows 11で実践するための手順を説明します。一つ一つのステップを丁寧に案内しますので、初めての方でも安心して進めてください。
## 1. このスクリプトの目的
このスクリプトは、PDFファイルに含まれる画像を取り除き、その結果としてファイルサイズを小さく（圧縮）するものです。例えば、資料の中で画像が不要な場合や、軽いファイルにしたいときに役立ちます。
## 2. Pythonのインストール
このスクリプトを使うには、まずPythonというツールをパソコンにインストールする必要があります。Windows 11では、次の手順で簡単にインストールできます。

**手順：**
1. Microsoft Storeを開く：
画面左下の「スタート」ボタン（Windowsアイコン）をクリック。
 - 検索バーに「Microsoft Store」と入力し、表示されたアプリを開きます。

2. Pythonを検索：
 - Microsoft Storeの上部にある検索バーに「Python」と入力。
 - 最新バージョン（例：Python 3.12）を選択します。

3. インストール：
 - 「入手」または「インストール」ボタンをクリックしてPythonをインストール。

4. 確認：
 - インストールが終わったら、スタートメニューに「Python」が追加されているか確認してください。

## 3. コマンドプロンプトの開き方
スクリプトを実行するには、コマンドプロンプトというツールを使います。これは、Windowsで命令を入力するための黒い画面です。

**手順：**
1. コマンドプロンプトを開く：
  - スタートボタンをクリックし、検索バーに「cmd」と入力。
  - 「コマンドプロンプト」が表示されたら、それをクリックして開きます。
2. 準備完了：
  - 黒い画面が表示されたら、次のステップに進む準備ができています。

## 4. 必要なライブラリのインストール
このスクリプトでは、PDFを操作するためにPyPDF2とpikepdfという2つの追加ツール（ライブラリ）が必要です。これらをインストールします。

**手順：**
1. コマンドプロンプトでコマンドを実行：
  - コマンドプロンプトを開いた状態で、次のコマンドをそのまま入力し、Enterキーを押します：
```
pip install PyPDF2 pikepdf
```
2. インストールの確認：
  - しばらく待つと、画面に「Successfully installed」と表示されれば成功です。何かエラーが出た場合は、インターネットで「pip install エラー」と検索して解決方法を探してみてください。

## 5. スクリプトの保存
次に、提供されたスクリプトをパソコンに保存します。このスクリプトが、PDFから画像を削除する実際の処理を行います。

**手順：**
1. テキストエディタを開く：
  - Windows 11には「メモ帳」が標準で入っています。スタートメニューで「メモ帳」と検索して開きます。

2. スクリプトをコピーして貼り付け：
  - 以下のコードをすべてコピーし、メモ帳に貼り付けます：
```python
import io
from PyPDF2 import PdfReader, PdfWriter
from pikepdf import Pdf, ObjectStreamMode
from PyPDF2.generic import NullObject

def remove_images_from_pdf(input_path, output_path):
    # PyPDF2を使用してPDFを読み込む
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # pikepdfを使用してPDFを開く
    pdf = Pdf.open(input_path)

    for page_num in range(len(reader.pages)):
        # 各ページを処理
        page = reader.pages[page_num]
        
        # ページから全ての画像を削除
        if "/Resources" in page and "/XObject" in page["/Resources"]:
            xObject = page["/Resources"]["/XObject"].get_object()
            for obj in list(xObject.keys()):  # リストを使用して反復中の変更を避ける
                if xObject[obj]["/Subtype"] == "/Image":
                    xObject[obj] = NullObject()  # 空の辞書の代わりにNullObjectを使用
        
        # 修正したページを新しいPDFに追加
        writer.add_page(page)

    # 変更を適用して新しいPDFを保存
    with io.BytesIO() as output_buffer:
        writer.write(output_buffer)
        output_buffer.seek(0)
        
        # pikepdfを使用して最終的なPDFを圧縮
        pdf_output = Pdf.open(output_buffer)
        pdf_output.save(output_path, compress_streams=True, object_stream_mode=ObjectStreamMode.generate)

    print(f"画像を削除し、圧縮したPDFを {output_path} に保存しました。")

# 使用例
input_file = "input.pdf"
output_file = "output_no_images.pdf"
remove_images_from_pdf(input_file, output_file)
```

3. ファイルとして保存：
  - メモ帳のメニューで「ファイル」→「名前を付けて保存」を選択。
  - ファイル名を「remove_images_from_pdf.py」と入力（.pyを必ず付ける）。
  - 保存先はデスクトップやドキュメントフォルダなど、わかりやすい場所を選び、「保存」をクリック。

## 6. PDFファイルの準備
スクリプトを実行する前に、画像を削除したいPDFファイルを用意します。

**手順：**
1. PDFを用意：
  - 画像が含まれているPDFファイルを準備します。例えば「input.pdf」という名前で保存。

2. 配置：
  - このPDFを、スクリプト（remove_images_from_pdf.py）と同じフォルダに置くのが簡単です。たとえば、デスクトップにスクリプトを保存したなら、PDFもデスクトップに置きます。
  - 別の場所に置く場合は、PDFのフルパス（例：C:\Users\ユーザー名\Documents\input.pdf）を後で使うのでメモしておきます。

## 7. スクリプトの実行
準備ができたら、スクリプトを実行してPDFから画像を削除します。

**手順：**
1. コマンドプロンプトでフォルダに移動：
  - スクリプトを保存した場所に移動します。たとえば、デスクトップに保存した場合：
```
cd C:\Users\ユーザー名\Desktop
```
  - ※「ユーザー名」は自分のWindowsのユーザー名に置き換えてください。わからない場合は、エクスプローラーでデスクトップのフルパスを確認できます。

2. スクリプトを実行：
  - 次のコマンドを入力してEnterキーを押します：
```
python remove_images_from_pdf.py input.pdf output_no_images.pdf
```
  - 説明：
    - input.pdf：画像を削除したいPDFファイルの名前（同じフォルダにある場合）。別の場所にある場合はフルパスを指定。
    - output_no_images.pdf：画像を削除した後の新しいPDFの名前。

3. 結果の確認：
  - 実行が成功すると、コマンドプロンプトに「画像を削除し、圧縮したPDFを output_no_images.pdf に保存しました。」と表示されます。
  - 保存先（例：デスクトップ）にoutput_no_images.pdfができているか確認してください。

### 具体例：
PDFが「C:\Users\太郎\Documents\sample.pdf」にある場合：
```
python remove_images_from_pdf.py C:\Users\太郎\Documents\sample.pdf C:\Users\太郎\Documents\sample_no_images.pdf
```
これで、sample_no_images.pdfに画像が削除されたPDFが保存されます。

## 8. もしうまくいかない場合（トラブルシューティング）
エラーが出た場合、以下の点をチェックしてください：
  - Pythonが動いているか：
     - コマンドプロンプトでpython --versionと入力し、バージョン（例：Python 3.12.0）が表示されるか確認。
  - ライブラリがインストールされているか：
     - pip listと入力し、「PyPDF2」や「pikepdf」がリストにあるか確認。
  - フォルダが正しいか：
     - cdコマンドで正しいフォルダに移動しているか確認。間違えた場合は再度入力。
  - ファイル名やパスが間違っていないか：
     - input.pdfが存在するか、フルパスに誤りがないか確認。

## 9. まとめ
お疲れ様でした！これで以下の手順を完了しました：
1. Pythonをインストール
2. コマンドプロンプトを開く
3. PyPDF2とpikepdfをインストール
4. スクリプトを保存
5. PDFを準備
6. スクリプトを実行して画像を削除＆圧縮

これで、PDFから画像を取り除き、軽いファイルを作ることができました。不明点があれば、「Python 使い方」などで検索してみるとさらに詳しい情報が見つかります。ぜひ試してみてください！

