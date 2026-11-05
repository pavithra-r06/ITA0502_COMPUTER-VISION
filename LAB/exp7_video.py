import cv2

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found!")
    exit()

# Normal speed
delay = 30

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(delay) & 0xFF

    # S = Slow motion
    if key == ord('s'):
        delay = 150
        print("Slow motion")

    # F = Fast motion
    elif key == ord('f'):
        delay = 1
        print("Fast motion")

    # N = Normal speed
    elif key == ord('n'):
        delay = 30
        print("Normal speed")

    # Q = Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()