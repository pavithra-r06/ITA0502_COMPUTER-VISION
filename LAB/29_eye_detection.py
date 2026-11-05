import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eyes = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
for (x,y,w,h) in face.detectMultiScale(gray, 1.1, 5):
    roi_gray, roi_color = gray[y:y+h,x:x+w], img[y:y+h,x:x+w]
    for (ex,ey,ew,eh) in eyes.detectMultiScale(roi_gray, 1.1, 5):
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
cv2.imshow("Eye detection", img); cv2.imwrite("eye_detection.jpg", img)
cv2.waitKey(0); cv2.destroyAllWindows()
