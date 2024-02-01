from PIL import Image; import os
cwd = os.getcwd()
directory = cwd
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        prefix = filename.split(".jpg")[0]
        im = Image.open(filename)
        im.save(prefix + '.pdf') 
    elif filename.endswith(".png"):
        prefix1 = filename.split(".png")[0]    
        im = Image.open(filename)
        im.save(prefix1 + '.pdf')
    
