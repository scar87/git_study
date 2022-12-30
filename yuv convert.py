import cv2
img = cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) #cvtColor : color space 변환을 위한 함수
#3개의 채널로 분리
cv2.imshow('Ychannel',yuv_img[:,:,0]) # grayscale과 동일하게 출력 = 밝기
cv2.imshow('Uchannel',yuv_img[:,:,1]) # color infomation(Blue)
cv2.imshow('Vchannel',yuv_img[:,:,2]) # color information(red)
cv2.waitKey()
cv2.destroyAllWindows()
