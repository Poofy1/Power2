#python 3.8.5
#Cropped and power of two dataset creator
import os
from cv2 import cv2
import PIL
from PIL import Image

start = "E:/PYTHONSTOARGE/DATASET/"
final = "E:/PYTHONSTOARGE/512DATASET/"
resolution = 512

for i, filename in enumerate(os.listdir(start)):
    try: 
        imgCrop = Image.open(f'{start}{str(filename)}')
        imgCrop = imgCrop.convert('RGB')
        w, h = imgCrop.size
        if h > w:
            Dif = int((h - w)/2)
            imgCrop.crop((0, 0 + Dif, w, w + Dif)).save(f'{final}{str(i)}.jpg')
        elif w > h:
            Dif = int((w - h)/2)
            imgCrop.crop((0 + Dif, 0, h + Dif, h)).save(f'{final}{str(i)}.jpg')
        else:
            imgCrop.save(f'{final}{str(i)}.jpg')

        img_array = cv2.imread(f'{final}{str(i)}.jpg')
        new_array = cv2.resize(img_array, (resolution, resolution))
        cv2.imwrite(f'{final}{str(i)}.jpg', new_array)
        print("Image: {}".format(i))
    except:
        print("Image: {} ERROR".format(i))
