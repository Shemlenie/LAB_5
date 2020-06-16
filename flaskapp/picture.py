import base64
import io
from PIL import Image, ImageEnhance
import numpy as np

def merge(img_1, img_2):
    img = Image.new('RGB', (256, 256*3))
    img1 = Image.open('1.jfif')
    img2 = Image.open('2.jfif')
    img.paste(img1, (0,0))
    img.paste(img2, (0,256))
    return img

def stringToRGB(base64_string, num):
    imgdata = base64.b64decode(str(base64_string))
    filename = f'static/picha_{num}.jpeg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)