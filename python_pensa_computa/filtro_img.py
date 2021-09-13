from PIL import Image, ImageFilter

abrir = Image.open('/home/jhorsax/Escritorio/python_platz/arch.png')

after = abrir.filter(ImageFilter.BLUR)
after.save("new.png")

"""im = Image.open('/home/jhorsax/Escritorio/python_platz/arch.png', mode='r')
im.save('new_im.jpg', quality = 95)"""