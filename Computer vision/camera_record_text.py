import cv2

# Open camera
cap = cv2.VideoCapture(0)

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print("Recording with text... Press 'q' to stop")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add ONLY text
    cv2.putText(frame, "Camera recording be careful ",
                (20, 40),                  # position (x, y)
                cv2.FONT_HERSHEY_SIMPLEX,  # font
                1,                         # font size
                (0, 255, 0),               # color (green)
                2)                         # thickness

    out.write(frame)       # save frame
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved with text")
