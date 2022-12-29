#image 출력
import cv2 #opencv 라이브러리 import

####!!!!!!!!
# windows  이미지 파일명 한글 쓰지말것(UTF8, EUC-KR 한글인식 문제)
####!!!!!!!!

# for windows only
# img = cv2.imread('c:\\Users\\scar87\\OneDrive\\사진\\짤\\파딱KakaoTalk_20220319_164800647.png')
# for all os
# img = cv2.imread('c:/Users/scar87/OneDrive/사진/짤/파딱KakaoTalk_20220319_164800647.png')

img_color = cv2.imread('./images/a.png', cv2.IMREAD_COLOR)
img_gray = cv2.imread('./images/a.png', cv2.IMREAD_GRAYSCALE)
img_unchange = cv2.imread('./images/a.png', cv2.IMREAD_UNCHANGED)
# if img is None:
#     print('image read fail')
#     exit(0)

cv2.imshow('Show images0', img_color) #출력 화면을 Show images로 저장
cv2.imshow('Show images1', img_gray) #출력 화면을 Show images로 저장
cv2.imshow('Show images2', img_unchange) #출력 화면을 Show images로 저장
cv2.waitKey() #waitKey : 키보드 바인딩을 위한 함수
cv2.destroyAllWindows()
# print('gggg\nhhhhh')