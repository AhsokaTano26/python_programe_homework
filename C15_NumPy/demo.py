import glob 
import numpy as np 
from cv2 import imread, imwrite   #opencv-python  

imgs, heights, widths = [],[],[]
for f in glob.glob("pictures/*.jpg"):
    img = imread(f,-1)
    print("original: ", img.shape)
    h,w = img.shape[:2]
    heights.append(h)
    widths.append(w)
    imgs.append(img)

minHeight = min(heights)
minWidth = min(widths)
for i,x in enumerate(imgs):
    imgs[i] = x[:minHeight:3,:minWidth:3]
    print("thumbnail:", imgs[i].shape)

img0 = np.concatenate(imgs[:3],1)
img1 = np.concatenate(imgs[3:6],1)
img2 = np.concatenate(imgs[6:],1)
img9 = np.concatenate([img0,img1,img2],0)
print("3x3_0,shape:",img9.shape)
imwrite("3x3_0.jpg",img9)


 


