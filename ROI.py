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
    if event == cv2.EVENT_LBUTTONDOWN: #왼쪽버튼 누름
        drag = True
        default_x = x
        default_y = y
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
        if drag:
            draw= True
            defalut_x = x
            default_y = y
        elif event == cv2.EVENT_MOUSEMOVE: #마우스 이동
            if drag:
                draw = img.copy() # img 복제
                cv2.rectangle(draw, (default_x, default_y),(x,y), blue, 3)
                cv2.imshow("img", draw)
        elif event == cv2.EVENT_LBUTTONUP: #왼쪽버튼 땜
            if drag:
                drag = False
                w = x - default_x
                h = y - default_y
                if w > 0 and h > 0:
                    draw =img.copy()
                    cv2.rectangle(draw, (default_x, default_y),(x,y), blue, 3)
                    cv2.imshow("img", draw)
                    roi = img[default_y:default_y+h, default_x+w]
                    cv2.imshow("drag",roi) # drag 한 창 생성
                    cv2.imwrite('drag.jpg', roi) #drag 내용 저장
                else:
                    cv2.imshow('img,img')

cv2.setMouseCallback('img',Mouse)
cv2.waitKey()
cv2.destroyAllWindows()