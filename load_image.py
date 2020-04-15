import numpy as np
import cv2
import math

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image',img)

print(img.max())
print(img.min())

#print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img.item(i,j)
        if a>155:
            img.itemset((i,j),255)
        else:
            img.itemset((i,j),0)
        
cv2.imshow('output image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()