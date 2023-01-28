import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

kernel_3 = np.ones((3,3), np.float32) / 9
kernel_5 = np.ones((5,5), np.float32) / 25

kernel_3_output = cv2.filter2D(img, -1, kernel_3)
kernel_5_output = cv2.filter2D(img, -1, kernel_5)

cv2.imshow('Img', img) #기본이미지
cv2.imshow('kernel_3', kernel_3_output) #3*3블러링 이미지
cv2.imshow('kernel_5', kernel_5_output) #5*5블러링 이미지

cv2.waitKey()
cv2.destyroyAllWindows()