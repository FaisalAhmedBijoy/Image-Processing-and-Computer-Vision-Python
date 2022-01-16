import numpy as np
import cv2
img=cv2.imread('lena.jpg',0)

cv2.imshow('input',img)

minmax_img=np.zeros((img.shape[0],img.shape[1]),dtype='uint8')

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        xinput=img.item(i,j)
        minmax_img[i,j]=255*(img[i,j]-np.min(img)) / (np.max(img)-np.min(img))  

cv2.imshow('min max',minmax_img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

