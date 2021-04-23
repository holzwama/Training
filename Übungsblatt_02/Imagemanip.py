import PIL.Image as Imagepip install Pillow
img = Image.open("bilder/lena.pgm")
cols, rows = img.size # 512, 512
v = img.getpixel((cols-1, rows-1)) # hole Wert eines Pixel (0..255)
img.putpixel((0,0), v) # setze Pixel von rechts unten nach links oben
img.save("/tmp/komisch.pgm")