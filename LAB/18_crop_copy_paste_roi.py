import cv2, sys
img = cv2.imread(sys.argv[1] if len(sys.argv) > 1 else "image.jpg")
if img is None: raise SystemExit("Image not found. Pass an image path.")
# Select ROI with the mouse, then press ENTER or SPACE.
x, y, w, h = cv2.selectROI("Select region of interest", img, False)
cv2.destroyWindow("Select region of interest")
if w == 0 or h == 0: raise SystemExit("No ROI selected.")
roi = img[y:y+h, x:x+w].copy()
result = img.copy()
# Paste the selected region into the top-left corner (adjust if necessary).
ph, pw = min(h, result.shape[0]), min(w, result.shape[1])
result[0:ph, 0:pw] = roi[0:ph, 0:pw]
cv2.imshow("Cropped ROI", roi); cv2.imshow("Copied and pasted ROI", result)
cv2.imwrite("cropped_roi.jpg", roi); cv2.imwrite("roi_pasted.jpg", result)
cv2.waitKey(0); cv2.destroyAllWindows()
