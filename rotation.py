import cv2
import numpy as np

img= cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')
row, col = img.shape[:2]
rotation = cv2.getRotationMatrix2D((col/2, row/2), 20, 1)
img_rotation= cv2.warpAffine(img, rotation, (col, row))
cv2.imshow('Rotation', img_rotation)
cv2.waitKey()
cv2.destroyAllWindows()

#shape는 row, column, channle로 구성