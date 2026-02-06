import cv2

# Open camera
cap = cv2.VideoCapture(0)

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print("Recording... Press 'q' to stop")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)          # Save frame
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved as output.avi")
