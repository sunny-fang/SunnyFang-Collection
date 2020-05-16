#%%
import os
os.chdir('D:\\研究所(2019.9.23)\\碩一上\\DIGI\\專案\\pic')
# 讀圖片的RGB
import cv2 
# 讀取圖像，直接是numpy矩陣格式 
img = cv2.imread('wood01.jpg',1) # 0表示讀入灰色圖片，1表示讀入彩色圖片 
cv2.imshow('image',img) # 顯示圖像 
print(img.shape) # （height，width，channel） 
print(img.size) # 像素數量 print(img.dtype) # 數據類型 
print(img) # 列印圖像的numpy數組，3緯數組
#%%
# 網址1:https://colour.readthedocs.io/en/v0.3.13/generated/colour.sRGB_to_XYZ.html
# 網址2:https://colour.readthedocs.io/en/v0.3.7/colour.html
# 網址3:https://colour.readthedocs.io/en/v0.3.13/generated/colour.Lab_to_LCHab.html?highlight=lch#colour.Lab_to_LCHab
# sRGB_to_XYZ
#import colormath
#from colormath.color_objects import LabColor, XYZColor
#from colormath.color_conversions import convert_color
import colour
import numpy as np
sRGB = [200/255,150/255,100/255]
RGB = np.array(sRGB)
XYZ = colour.sRGB_to_XYZ(sRGB)
Lab = colour.XYZ_to_Lab(XYZ)
LCHab = colour.Lab_to_LCHab(Lab)
L = int(LCHab[0]);C = int(LCHab[1]);ab = int(LCHab[2])
#%%
LCHab = ['41','59','27']
LCHab = np.array(LCHab)
L = int(LCHab[0]);C = int(LCHab[1]);ab = int(LCHab[2])
#%%
r = 255;g = 89;b = 0
sRGB = [r/255,g/255,b/255]
RGB = np.array(sRGB)
XYZ = colour.sRGB_to_XYZ(sRGB)
Lab = colour.XYZ_to_Lab(XYZ)
LCHab = colour.Lab_to_LCHab(Lab)
L = int(LCHab[0]);C = int(LCHab[1]);ab = int(LCHab[2])
print([L,C,ab])
if C<40:# 1
    if L<10:
        print('black')
    elif L>90:
        print('white')
    else:
        print('gray')
elif ab<45:# 2
    if L<30:
        print('brown')
    elif L>70:
        print('pink')
    else:
        print('red')
elif ab<75:# 3
    if L<30:
        print('brown')
    else:
        print('orange')
elif ab<105:# 4
    print('yellow')
elif ab<210:# 5
    print('green')
elif ab<315:# 6
    print('blue')
elif ab>330:# 7
    if L>50:
        print('pink')
    else:
        print('purple')
else:
    print('purple')
#%%






















