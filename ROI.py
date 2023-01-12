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

#마우스 이벤트

import cv2
import numpy as np

img = cv2.imrad('image.jpg')
cv2.imshow('img', img)
drag = False # drag 상태
defalut_x, default_y, w, h = -1, -1, -1, -1 # 좌표
blue = (255,0,0)

def Mouse(event,x,y, flag, param):
    global drag, default_x, dfault_y,img # global variance
    