import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(gray, 1.1, 5, minSize=(30,30))
for (x,y,w,h) in faces: cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
print("Number of faces:", len(faces))
cv2.imshow("Face detection", img); cv2.imwrite("face_detection.jpg", img)
cv2.waitKey(0); cv2.destroyAllWindows()
