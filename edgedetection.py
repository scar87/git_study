import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

# 기분 미분 kernel 생성
G_x = np.array([[-1,1]])
G_y = np.array([[-1], [1]])

#필터적용
edge_x = cv2.filter2D(img, -1, G_x)
edge_y = cv2.filter2D(img, -1, G_y)

cv2.imshow('Edge_x', edge_x) #수평 에지
cv2.imshow('Edge_y', edge_y) #수직 에지

cv2.waitKey()