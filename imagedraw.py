import cv2
import numpy as np

img = np.full((350,350,3), 255 , dtype = np.uint8) # 350x350 크기의 흰 이미지

cv2.line(img, (50,50), (100,50),(0,0,255)) #Red
cv2.line(img, (150,50), (200,50), (0,255,0)) #Green
cv2.line(img, (250,50), (300,50), (255,0,0)) #Blue

cv2.line(img, (50,100), (300, 100), (0,255,255), 5) # Yellow = Red + Green/두께5
cv2.line(img, (50,150), (300, 150), (255,0,255), 5) # Pink = Red + Blue
cv2.line(img, (50,200), (300, 200), (255,255.0), 5) # Skyblue = Green + Blue

cv2.line(img, (50,250), (300, 300), (0,0,0), 10, cv2.LINE_8) # Black/두께 10/계단 현상
cv2.line(img, (50,300), (300, 100), (0,0,0), 10, cv2.LINE_AA) # 계단 현상 없이 매끄럽게 출력

cv2.imshow('Line', img)
cv2.waitKey()
cv2.destroyAllWindows()