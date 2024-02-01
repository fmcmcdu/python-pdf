from PIL import Image
name = int(input("Введите количество изображений "))
for pdfs in range (name):
    pdfs = [ 
    name := input("Введите имя изображения (с расширением) "),
    image_1 := Image.open(name),
    im_1 := image_1.convert('RGB'),
    name := input("Введите имя нового файла (без расширения) "),
    ext := ".pdf",
    im_1.save(name + ext)]