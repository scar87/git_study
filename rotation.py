import cv2
import numpy as np

img= cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')
row, col = img.shape[:2]
# rotation = cv2.getRotationMatrix2D((col/2, row/2), 20, 1)
# img_rotation= cv2.warpAffine(img, rotation, (col, row))
# cv2.imshow('Rotation', img_rotation)
# cv2.waitKey()
# cv2.destroyAllWindows()

#shape는 row, column, channle로 구성

#이미지를잘리지않게출력
translation = np.float32([[1,0,(col/2)],[0,1,(row/20)]])
rotation = cv2.getRotationMatrix2D((col/2, row/2), 20, 1)
img_translation = cv2.warpAffine(img, translation,(col*2,row*2))
img_rotation = cv2.warpAffine(img_translation, rotation, (col*2,row*2))
cv2.imshow('Rotation2', img_rotation)
cv2.waitKey()
cv2.destroyAllWindows()