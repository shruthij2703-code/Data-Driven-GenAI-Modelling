import cv2

img = cv2.imread(r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img\paris.jpg", 0)
img1 = cv2.imread(r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\img1\girl.jpg", 0)


# Resize img1 to match img size
img1 = cv2.resize(img1, (img.shape[1], img.shape[0]))

# Add images
added_image = cv2.add(img, img1)

cv2.namedWindow("Added Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Added Image", 800, 600)

cv2.imshow("Added Image", added_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
