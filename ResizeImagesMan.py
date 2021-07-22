import os
from PIL import Image

f = r'D:\UNIVERSITY CONFERENCE\INTERNET B ROLL'

for file in os.listdir(f):
    f_img = f+"/"+file
    basewidth = 1920
    img = Image.open(f_img)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save(f_img)
