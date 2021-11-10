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

#img = cv2.imread("1st.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("Lena.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (SIZE, SIZE))
cv2.imshow("input", img)
cv2.waitKey(0)

#cv2.destroyAllWindows()

sobel_x = np.array([[-1, 0, 1],
           [-2, 0, 2],
           [-1, 0, 1]])

sobel_y = np.array([[1, 2, 1],
           [0, 0, 0],
           [-1, -2, -1]])

sx = cv2.filter2D(src=img, ddepth=-1, kernel=sobel_x)
#sx = normalize(sx)

cv2.imshow("sobel_x", sx)
cv2.waitKey(0)

sy = cv2.filter2D(src=img, ddepth=-1, kernel=sobel_y)
#sy = normalize(sy)

cv2.imshow("sobel_y", sy)
cv2.waitKey(0)

tr = 50

sx = normalize(sx)
sy = normalize(sy)

out = np.sqrt(np.multiply(sx, sx) + np.multiply(sy, sy))
out = normalize(out)
#out = np.array(out, dtype='uint8')
out[out>=tr] = 255
out[out<tr] = 0

cv2.imshow("output", out)
cv2.waitKey(0)

cv2.destroyAllWindows()