import cv2
img = cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#3개의채널로 분리
# cv2.imshow('HSVimage', hsv_img)
# cv2.waitKey()
# cv2.destroyAllwindows()
cv2.imshow('Hchannel',hsv_img[:,:,0]) #색상
cv2.imshow('Schannel',hsv_img[:,:,1]) #명도
cv2.imshow('Vchannel',hsv_img[:,:,2]) #채도
cv2.waitKey()
cv2.destroyAllWindows()