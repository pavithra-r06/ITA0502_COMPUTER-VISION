import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
out = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Binary", binary); cv2.imshow("Closing", out)
cv2.imwrite("closing.jpg", out); cv2.waitKey(0); cv2.destroyAllWindows()
