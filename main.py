from PIL import Image, ImageFilter
im = Image.open("bilde.jpg")
print(im.format, im.size, im.mode)
im.show()
izmers = (100, 69)
im.thumbnail(izmers)
im.save("bilde-maza.jpg", im.format)
#im.show()
im = im.rotate(45)
#rotate(20) rāda error.
#im.show()
r, g, b = im.split()

#im = Image.merge("RGB", (g,r,b)). NESTRĀDĀ
#im.show()
im = im.filter(ImageFilter.CONTOUR)
im = im.filter(ImageFilter.EDGE_ENHANCE)
#im.show()
cropped = im.crop((1,2,100,50))
cropped.show()
