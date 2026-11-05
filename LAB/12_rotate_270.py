import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
out = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 270 degrees clockwise
cv2.imshow("Original", img); cv2.imshow("270 degree clockwise", out)
cv2.imwrite("output_270.jpg", out); cv2.waitKey(0); cv2.destroyAllWindows()
