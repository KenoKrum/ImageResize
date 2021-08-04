import os
import PIL
from PIL import Image

f = r'D:\UNIVERSITY CONFERENCE\INTERNET B ROLL\Testing'


for file in os.listdir(f):
    f_img = f+"/"+file
    img = PIL.Image.open(f_img)
    width, height = img.size

    if width >= height:
        basewidth = 1920
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(f_img)

    if height > width:
        baseheight = 1080
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight), Image.ANTIALIAS)
        img.save(f_img)

