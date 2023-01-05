import cv2

cap = cv2.VideoCapture(0) #카메라연결
if not cap.isOpened(): #초기화확인
    raise loError("Can't open webcam")
while True:
    ret, frame = cap.read()#