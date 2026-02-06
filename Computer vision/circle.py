import cv2
img = cv2.imread(r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img\paris.jpg", 0)
cv2.imshow('name',img)

cv2.circle(img,(50,70),45,(255,0,0),5)
#circele has 5 parameters
#1 image,ceneter_cordinates,radius,colour,thickness
cv2.imshow('win2',img)
cv2.imwrite('img\paris_new.jpg',img)#i'm write is to save the image
cv2.waitKey(0)
cv2.destroyAllWindows()
