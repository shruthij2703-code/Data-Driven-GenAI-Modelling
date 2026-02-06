import cv2
img = cv2.imread(r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img\paris.jpg", 0)
cv2.imshow('name',img)

cv2.line(img,(50,70),(200,50),(255,0,0),5)
#line has 6 parameters
#1
cv2.imshow('win2',img)
cv2.imwrite('img\paris_new.jpg',img)#i'm write is to save the image
cv2.waitKey(0)
cv2.destroyAllWindows()
