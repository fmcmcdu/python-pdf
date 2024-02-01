import pypdfium2 as pdfium
name = input("Введите имя документа (без расширения) ")
ext = ".pdf"
pdf = pdfium.PdfDocument(name + ext)
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=4).to_pil()
    name = input("Введите имя изображения (без расширения) ")
    ext = ".jpg"
    image.save(name + ext), (i+1)