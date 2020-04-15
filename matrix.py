# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:36:35 2020

@author: Faisal Ahmed
"""

import cv2
import numpy as np
inp = cv2.imread('phone.png',0)
cv2.imshow('input image',inp)
show = inp.copy()
#inp = [[1,2,3],[4,5,6]]
fil = [[10,20],
       [30,40]]
m1=inp.shape[0]
n1=inp.shape[1]
m2=2
n2=2
#npa = np.asarray(inp, dtype=np.float32)
npa = np.asarray(inp)
 
print(npa)
 
#2: calculating final output size
nrow = m1 + m2 -1
ncol = n1 + n2 -1
 
#3:Zero Padded filter matrix
f=[]
for i in range(0,nrow):
    f.append([])
    for j in range(0,ncol):
        f[i].append(0)
#print(f)        
 
difi = nrow - m2
difj = ncol - n2
for i in range(0,nrow):
    for j in range(0,ncol):
        if((i-difi) in range(0,m2) and (j) in range(0,n2)):
            f[i][j] = fil[i-difi][j]
#print(f)

def toeplitz(mat,rowsize,colsize):
    a=[]
    for i in range(0,rowsize):
        a.append([])
        for j in range(0,colsize):
            a[i].append(0)
           
    for i in range(0,rowsize):
        for j in range(0,colsize):
            if((i-j)>=0):
                a[i][j] = mat[i-j]
               
    return a
new = toeplitz(f[2],ncol,n1)
#print(new)
 
def zero_matrix(m,n):
    mat =[]
    for i in range(0,m):
        mat.append([])
        for j in range(0,n):
            mat[i].append(0)
    return mat
 
#4: create toeplitz matrix from zero padded filter
toeplitz_matrix = []
for i in range(0,len(f)):
    new = toeplitz(f[nrow-1-i],ncol,n1)
    toeplitz_matrix.append(new)
print(toeplitz_matrix)
print('')
       
#5: create dobly blocked toeplitz matrix
doubly_blocked = toeplitz(toeplitz_matrix,nrow,m1)  
for i in range(0,len(doubly_blocked)):
    for j in range(0,len(doubly_blocked[i])):
        if(doubly_blocked[i][j]==0):
            doubly_blocked[i][j] = zero_matrix(ncol,n1)
npa = np.asarray(doubly_blocked)
#print(npa)
 
for i in range(0,len(npa)):
    a = np.array(npa[i][0])
    for j in range(1,len(npa[i])):
        b = np.array(npa[i][j])
        a = np.concatenate((a, b),axis = 1)
    if(i==0):
        val = a
        continue
    val = np.concatenate((val,a))
#print(val)
input_vector=[]
for i in range(m1-1,-1,-1):
    for j in range(n1):
        input_vector.append(inp.item(i,j))
input_vector = np.asanyarray(input_vector)
output= np.dot(val,input_vector)
print(output)
outp= zero_matrix(nrow,ncol)
for i in range(m1):
    for j in range(n1):
        outp[i][j] = output[(nrow -1-i)*ncol+j]
        show.itemset((i,j),(1/100)*outp[i][j] )
cv2.imshow('output',show)
cv2.waitKey(0)
cv2.destroyAllWindows()