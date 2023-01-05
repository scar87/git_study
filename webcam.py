# #이미지 저장
# import cv2

# cap = cv2.VideoCapture(0) #카메라연결
# if not cap.isOpened(): #초기화확인
#     raise IOError("Can't open webcam")
# while True:
#     ret, frame = cap.read() #프레임 읽기
#     #framecv2.resize(frame, None, fx=0.7, fy=0.7)
#     cv2.imshow('CAMERA',frame)
#     if cv2.waitKey(1) == 27: #ESC의 ASCII: 27
#         cv2.imwrite('output.jpg', frame)
#         break

# cap.release() #캡쳐 자원 반납
# cv2.destroyALLwindows()

#비디오 저장
import cv2
cap = cv2.VideoCapture(0) #카메라 장치 연결
form = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', form, 20.0, (640)) #filename, 인코딩 포맷 문자, fps, frame 크기
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame")
        break
    output.write(frame) #파일저장
    cv2, imshow('CAMERA', frame)
    if cv2.waitKey(1) == 27:
        break
output.release() #파일 닫기
cap.release()
cv2.destroyAllWindows()