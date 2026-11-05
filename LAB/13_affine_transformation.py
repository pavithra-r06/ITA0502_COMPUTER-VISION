import cv2, numpy as np, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
h, w = img.shape[:2]
src = np.float32([[50, 50], [w-50, 50], [50, h-50]])
dst = np.float32([[10, 100], [w-100, 50], [100, h-100]])
M = cv2.getAffineTransform(src, dst)
out = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Original", img); cv2.imshow("Affine transformation", out)
cv2.imwrite("affine_output.jpg", out); cv2.waitKey(0); cv2.destroyAllWindows()
