import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
out = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Original grayscale", gray); cv2.imshow("Black-hat", out)
cv2.imwrite("black_hat.jpg", out); cv2.waitKey(0); cv2.destroyAllWindows()
