import pyqrcode
from PIL import Image
from pyqrcode import QRCode
url=pyqrcode.QRCode("http://pravesh.epizy.com/loginsystem",error='H')
url.png('test.png',scale=10)
im=Image.open('test.png')
im=im.convert("RGBA")
logo=Image.open('logo.png')
box=(200,200,300,300)
im.crop(box)
region=logo
region=region.resize((box[2]-box[0],box[3]-box[1]))
im.paste(region,box)
im.show()

