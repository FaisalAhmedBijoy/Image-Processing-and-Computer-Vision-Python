import numpy as np
import cv2
import math
img = cv2.imread('kuet.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input image',img)
print(img.max())
print(img.min())
print(img.shape)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a = img.item(i,j)
        y = 3
        c = 255**(y-1)
        if a >= 0 and a <= 60:
            img.itemset((i,j),a**y/c+20000)
        elif a >= 61 and a <= 120:
            img.itemset((i,j),a**y/c+10)
        elif a >= 121 and a <= 200:
            img.itemset((i,j),a**y/c-10)
        else:
            img.itemset((i,j),a**y/c-20)

cv2.imshow('output image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()