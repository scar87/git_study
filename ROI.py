#좌표지정
import cv2
import numpy as np

img = cv2.imread('image.jpg')
x = 350; y = 125
w = 260; h = 260
roi = img[y:y+h, x:x+w]
cv2.rectangle(roi,(0,0), (h-1, w-1), (0,255,0),5)

cv2.imshow("IMAGE", img)
cv2.waitKey()
cv2.destroyAllWindows()