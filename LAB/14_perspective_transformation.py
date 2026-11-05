import cv2, numpy as np, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
h, w = img.shape[:2]
src = np.float32([[0,0], [w-1,0], [0,h-1], [w-1,h-1]])
dst = np.float32([[50,50], [w-80,20], [20,h-50], [w-20,h-20]])
M = cv2.getPerspectiveTransform(src, dst)
out = cv2.warpPerspective(img, M, (w, h))
cv2.imshow("Original", img); cv2.imshow("Perspective transformation", out)
cv2.imwrite("perspective_output.jpg", out); cv2.waitKey(0); cv2.destroyAllWindows()
