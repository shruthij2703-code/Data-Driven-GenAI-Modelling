import cv2

# Open the downloaded space video (YOUR PATH)
cap = cv2.VideoCapture(
    r"C:\Users\santh\OneDrive\Desktop\Computer_vision_work\planet.mp4"
)

# Check if video opened correctly
if not cap.isOpened():
    print("Error: Could not open video")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Video writer (output file)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, fps, (width, height))

print("Processing video...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Add text on video
    cv2.putText(
        frame,
        "Earth: The Unique Home",
        (50, 50),                    # position (x, y)
        cv2.FONT_HERSHEY_SIMPLEX,    # font
        1,                           # font size
        (0, 255, 0),                 # color (green)
        2                            # thickness
    )

    out.write(frame)

cap.release()
out.release()

print("Video saved as output.avi with text")
