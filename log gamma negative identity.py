# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 01:24:49 2020

@author: NLP Lab
"""

import numpy as np
import cv2
import math

img=cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
out=img.copy()
out2=img.copy()
out3=img.copy()
out4=img.copy()
out5=img.copy()

cv2.imshow('input image ',img )
c=31.875
gamma=0.5
for i in range (img.shape[0] ):
    for j in range (img.shape[1]):
        a=img.item(i,j) 
        
        
        
        #log
        out.itemset((i,j), c*math.log(a+1))
        
        #loginv
        #out2.itemset((i,j),c* math.pow(2,a+1))
        out2.itemset( (i,j),math.pow(2, a/c -1))
        
        #gamma
        out3.itemset((i,j),c* math.pow(a,gamma))
        
        #negative image :L-1-r
        out4.itemset( (i,j),255-a )
        
        #identity transformation : input =output : s=r
        out5.itemset((i,j),a)
        

cv2.imshow('output image 1 : log ',out)        
cv2.imshow('output image 2 : invlog ',out2)
cv2.imshow('output image 3 : gamma',out3)
cv2.imshow('output image 4: Negative',out4)

cv2.waitKey(0)
cv2.destroyAllwindows(0)

