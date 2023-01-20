# # import cv2
# # import numpy as np

# # img =np.full((300,300,3), 255, dtype =np.uint8)
# # title = "Mouse Event"
# # cv2.imshow(title,img)

# # def Mouse(event, x, y, flag, param):
# #     if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼 클릭
# #         cv2.circle(img, (x,y), 15, (255,0,0), -1)
# #         cv2.imshow(title, img)
# # cv2.setMouseCallback(title, Mouse)
# # while True:
# #     if cv2. waitKey() == 27:
# #         break
# # cv2.destroyAllWindows

# #이벤트 처리하는 함수(Mouse)선언후 cv2.setMouseCallback()에 이벤트 처리 함수 인자로넣어 이벤트 처리가 이루어지도록 작동하는 코드


# import cv2
# import numpy as np

# impg = np.full((300,300,3),255, dtype =np.unit8)
# title ="Mouse & Flag Event"
# cv2.imshoW(title,img)

# color = {'red' : (0,0,255),'green' : (0,255,0),'blue' :(255,0,0), 'black': (0,0,0)}

# def Mouse(event, x,y,flag, param):
#     output= color['black']
#     if event == cv2.EVENT_LBUTTONDOWN : #왼쪽버튼 클릭
#         if flag & cv2.EVENT_FLAG_ALTKEY: #Alt 누르면 Red
#             output = color['red']
#         elif flag & cv2.EVENT_FLAG_CTRLKEY : #Ctrl 누르면 Green
#             output =color['green']
#         elif flag& cv2.EVENT_FLAG_SHIFTKEY : #Shift 누르면 Blue
#             output =color['blue']
#         cv2.circle(img,(x,y), 15, output,-1)
#         cv2.imshow(title,img)
# cv2.setMouseCallback(title, Mouse)

# while True:
#     if cv2.waitKey() == 27:
#         break
# cv2.destroyAllWindows

#-------------------------cv2.selectROI()--------------------

import cv2
import numpy as np

img= cv2.imread('d:/ws/img/images/image.jpg')
x,y,w,h =cv2.selectROI('image', img, False)

if w and h:
    roi =img[y:y+h, x:x+w]
    cv2.imshow('drag', roi)
    cv2.imwrite('drag.jpg', roi)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()