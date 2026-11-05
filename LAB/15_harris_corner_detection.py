import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.dilate(gray, None)
corners = cv2.cornerHarris(gray.astype("float32"), 2, 3, 0.04)
result = img.copy()
result[corners > 0.01 * corners.max()] = [0, 0, 255]
cv2.imshow("Harris corners", result); cv2.imwrite("harris_corners.jpg", result)
cv2.waitKey(0); cv2.destroyAllWindows()
