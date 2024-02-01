from PyPDF2 import PdfMerger
merger = PdfMerger()
name = int(input('Введите количество страниц '))
for pdfs in range(name):
    pdfs = [
    name := input("Введите имя файла (без расширения) "),
    ext := ".pdf",
    merger.append(name+ext)
    ]
name = input("Введите имя нового файла (без расширения) ")
ext = ".pdf"
merger.write(name+ext)
merger.close()