import cv2
import matplotlib.pyplot as plt
import numpy as np

SIZE=250

def normalize(img):
    nImg = np.zeros(img.shape)
    
    max_ = img.max()
    min_ = img.min()
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            nImg[i][j] = (img[i][j]-min_)/(max_-min_) * 255
    
    return nImg

img = cv2.imread("1st.png", cv2.IMREAD_GRAYSCALE)
#img = cv2.imread("Picture1.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (SIZE, SIZE))
cv2.imshow("input", img)
cv2.waitKey(0)

tr = 150

img[img>=tr] = 255
img[img<tr] = 0

cv2.imshow("binary", img)
cv2.waitKey(0)

kernel = np.array([[1, 1, 1],
           [1, 1, 1],
           [1, 1, 1]])

dil = cv2.dilate(img, kernel)
cv2.imshow("dilated", dil)
cv2.waitKey(0)

cv2.imshow("dilated_boundary", dil-img)
cv2.waitKey(0)

er = cv2.erode(img, kernel)
cv2.imshow("eroded", er)
cv2.waitKey(0)

cv2.imshow("eroded_boundary", img-er)
cv2.waitKey(0)


# Opening - Good for removing noise
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)
cv2.waitKey(0) 

# Closing - Good for removing noise
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Closing', closing)
cv2.waitKey(0)

cv2.destroyAllWindows()
