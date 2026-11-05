import cv2, sys
# Uses OpenCV's built-in HOG people detector as a simple moving-object demonstration.
# For reliable vehicle-only detection, use a trained vehicle/YOLO model.
path = sys.argv[1] if len(sys.argv) > 1 else "video.mp4"
cap = cv2.VideoCapture(path)
if not cap.isOpened(): raise SystemExit("Video not found or cannot be opened.")
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
print("Note: built-in HOG detects pedestrians, not vehicles. Replace detector with a vehicle-trained model for vehicle detection.")
while True:
    ok, frame = cap.read()
    if not ok: break
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8), padding=(8,8), scale=1.05)
    for (x,y,w,h) in boxes: cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Video detection demo (pedestrian HOG)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
cap.release(); cv2.destroyAllWindows()
