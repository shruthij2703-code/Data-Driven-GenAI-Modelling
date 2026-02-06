import cv2
img = cv2.imread(r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img\paris.jpg", 0)
cv2.imshow('name',img)
cv2.imwrite('Cimg\paris_new.jpg',img)#i'm write is to save the image
cv2.waitKey(0)
cv2.destroyAllWindows()
