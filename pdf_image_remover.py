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
