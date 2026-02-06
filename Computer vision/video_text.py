import cv2
cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()
    cv2.putText(frame,'SHRUTHI',(40,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
