import base64
import io
from PIL import Image, ImageEnhance
import numpy as np

def merge(img_1, img_2):
    (width1, height1) = img_1.size
    (width2, height2) = img_2.size
    img = Image.new('RGB', (width1 + width2, height1 + height2))
    img.paste(img_1, (0,0))
    img.paste(img_2, (height1, 0))
    return img

def stringToRGB(base64_string, num):
    imgdata = base64.b64decode(str(base64_string))
    filename = f'static/picha_{num}.jpeg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)
