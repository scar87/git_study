import cv2
import numpy as np

img =np.full((300,300,3), 255, dtype =np.uint8)
title = "Mouse Event"
cv2.imshow(title,img)

def Mouse(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼 클릭
        cv2.circle(img, (x,y), 15, (255,0,0), -1)
        cv2.imshow(title, img)
cv2.setMouseCallback(title, Mouse)
while True:
    if cv2. waitKey() == 27:
        break
cv2.destroyAllWindows

#이벤트 처리하는 함수(Mouse)선언후 cv2.setMouseCallback()에 이벤트 처리 함수 인자로넣어 이벤트 처리가 이루어지도록 작동하는 코드