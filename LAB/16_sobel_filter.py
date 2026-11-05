import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
out = cv2.convertScaleAbs(cv2.addWeighted(cv2.convertScaleAbs(gx), .5, cv2.convertScaleAbs(gy), .5, 0))
cv2.imshow("Original", img); cv2.imshow("Sobel edges", out)
cv2.imwrite("sobel_output.jpg", out); cv2.waitKey(0); cv2.destroyAllWindows()
