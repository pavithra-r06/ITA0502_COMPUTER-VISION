import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
smile = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
for (x,y,w,h) in face.detectMultiScale(gray, 1.1, 5):
    roi_gray, roi_color = gray[y:y+h,x:x+w], img[y:y+h,x:x+w]
    smiles = smile.detectMultiScale(roi_gray, 1.7, 20, minSize=(25,15))
    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
cv2.imshow("Smile detection", img); cv2.imwrite("smile_detection.jpg", img)
cv2.waitKey(0); cv2.destroyAllWindows()
