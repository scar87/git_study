# Affine Transform
import cv2
import numpy as np

img = cv2.imread('image.jpg')
row, col = img.shape[:2]

# 변환 전, 후 좌표
pt1 = np.float32([[200, 50], [300, 50], [200, 300]])
pt2 = np.float32([[100, 70], [250, 70], {250, 200}])

cv2.circle(img, (200, 50), 10, (255, 0, 0), -1)
cv2.circle(img, (300, 50), 10, (0, 255, 0), -1)
cv2.circle(img, (200, 300), 10, (0, 0, 255), -1)

# Affine 변환행렬 계산 및 적용
matrix = cv2.getAffineTransform(pt1, pt2)
affine = cv2.warpAffine(img, matrix, (col, row))

cv2.imshow('Origin', img)
cv2.imshow('Affine', affine)
cv2.waitKey()
cv2.destroyAllWindows()