import cv2
img = cv2.imread(r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img\paris.jpg", 0)
cv2.imshow('name',img)

cv2.putText(img,'WELCOME TO THE WORLD OF MINE',(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
#image, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin
cv2.imshow('win2',img)
cv2.imwrite('img\paris_new.jpg',img)#i'm write is to save the image
cv2.waitKey(0)
cv2.destroyAllWindows()
