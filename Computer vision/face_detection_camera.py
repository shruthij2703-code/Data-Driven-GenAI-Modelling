import cv2
face_cascade=cv2.CascadeClassifier(r'C:\Users\santh\OneDrive\Desktop\Computer_vision_work\data\haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
while True:
   ret,frame=cam.read() 
   cv2.imshow('camera',frame)
   if cv2.waitKey(1) & 0xFF==ord('q'):
       break
cam.release()
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,w,h) in face:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,22,0),2)
cv2.imshow("faces",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
