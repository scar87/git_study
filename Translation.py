import cv2
import numpy as np

img = cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')
# 이미지 이동
row, col = img.shape[:2]
translation = np.float32([[1,0,40],[0,1,70]])
img_translation=cv2.warpAffine(img,translation, (row,col)) #warpAffine:이동할 매트릭스(translation) 적용
cv2.imshow('Translation', img_translation)
cv2.waitKey()
cv2.destroyAllWindows

#원래대로 복원
img = cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')
img_translation = cv2.warpAffine(img, translation, (col+40, row+70))
cv2.imshow('Translation2', img_translation)
cv2.waitKey()
cv2.destroyAllWindows