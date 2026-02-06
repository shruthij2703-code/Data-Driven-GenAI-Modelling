#FACE DETECTION

import cv2
face_cascade=cv2.CascadeClassifier(r'C:\Users\santh\OneDrive\Desktop\Computer_vision_work\data\haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img\jungkook.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("faces",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
