import cv2
import matplotlib.pyplot as plt
import numpy as np

SIZE=250

def image_normalize(img):
    output_image = np.zeros(img.shape)
    
    max_img = img.max()
    min_img = img.min()
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            output_image[i][j] = (img[i][j]-min_img)/(max_img-min_img) * 255
    
    return output_image


img = cv2.imread("Lena.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (SIZE, SIZE))
cv2.imshow("input", img)
cv2.waitKey(0)


sobel_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

sobel_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1,-2,-1]])

sx = cv2.filter2D(src=img, ddepth=-1, kernel=sobel_x)

cv2.imshow("sobel_x", sx)
cv2.waitKey(0)

sy = cv2.filter2D(src=img, ddepth=-1, kernel=sobel_y)


cv2.imshow("sobel_y", sy)
cv2.waitKey(0)

threshold = 50

sx = image_normalize(sx)
sy = image_normalize(sy)

output_image = np.sqrt(np.multiply(sx, sx) + np.multiply(sy, sy))
output_image = image_normalize(output_image)

output_image[output_image >=threshold] = 255
output_image[output_image <threshold] = 0

cv2.imshow("output", output_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
