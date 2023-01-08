# #선긋기
# import cv2
# import numpy as np

# img = np.full((350,350,3), 255 , dtype = np.uint8) # 350x350 크기의 흰 이미지

# cv2.line(img, (50,50), (100,50),(0,0,255)) #Red
# cv2.line(img, (150,50), (200,50), (0,255,0)) #Green
# cv2.line(img, (250,50), (300,50), (255,0,0)) #Blue

# cv2.line(img, (50,100), (300, 100), (0,255,255), 5) # Yellow = Red + Green/두께5
# cv2.line(img, (50,150), (300, 150), (255,0,255), 5) # Pink = Red + Blue
# cv2.line(img, (50,200), (300, 200), (255,255.0), 5) # Skyblue = Green + Blue

# cv2.line(img, (50,250), (300, 300), (0,0,0), 10, cv2.LINE_8) # Black/두께 10/계단 현상
# cv2.line(img, (50,300), (300, 100), (0,0,0), 10, cv2.LINE_AA) # 계단 현상 없이 매끄럽게 출력

# cv2.imshow('Line', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#===========================================


# import cv2
# import numpy as np

# img = np.full((450,450,3), 255, dtype = np.uint8)

# cv2.rectangle(img, (50,50), (150,150), (0,0,255))
# cv2.rectangle(img, (100,100),(250, 250),(0,255,0),5)
# cv2.rectangle(img, (200,200),(400,400), (255,0,0),-1) #Blue로 채우기

# cv2.imshow('Rectangle',img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#===========================================


# import cv2
# import numpy as np

# img =np.full((500,500,3),255, dtype=np.unit8)

# poly1 =np.array([[50,50],[200,200]]) #직선
# poly1 =np.array([[[350,50],[250,200],[450,200]]]) #삼각형
# poly1 =np.array([[[50,300],[300,200],[200,450],[50,450]]]) #사각형
# poly1 =np.array([[[350,250],[450,350],[300,450],[250,350]]])#오각형

# cv2.polylines(img, [poly1], True, (0,0,225))
# cv2.polylines(img, [poly1], True, (0,255,0))
# cv2.polylines(img, [poly1], True, (225,0,0))
# cv2.polylines(img, [poly1], False, (0,0,0)) #열린형태

# cv2.imshow('Polylines',img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#===========================================


import cv2
import numpy as np

img= np.full((50,450,3), 255, dtype = np.unit8)

cv2.circle(img,(100, 150),50, (0,0,255)) #원
cv2.circle(img,(200, 150), 75, (0,255,0), 5)
cv2.circle(img,(100, 150), 100, (0,0,255), -1)

cv2.ellipse(img,(100,300),(50,50), 0,0,360,(0,0,255)) #원
cv2.ellipse(img,(225,300),(50,50),0,0,180,(0,255,0)) #호
cv2.ellipse(img,(350,300),(50,50),0,0,180,(255,0,0), -1) #호

cv2.ellipes(img,(150, 400),(50,30),0,0,360,(0,0,0)) #타원
cv2.ellipse(img, (300, 400),(30,50),(45,0,360),(0,0,0),-1)

cv2.imshow('Circle',img)
cv2.waitKey()
cv2.destroyAllWindows()