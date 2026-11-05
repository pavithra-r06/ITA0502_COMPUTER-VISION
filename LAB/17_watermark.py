import cv2, sys
img_path = sys.argv[1] if len(sys.argv) > 1 else "image.jpg"
img = cv2.imread(img_path)
if img is None: raise SystemExit("Image not found. Pass an image path.")
watermark = img.copy()
cv2.putText(watermark, "WATERMARK", (30, img.shape[0]-30),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), 3, cv2.LINE_AA)
out = cv2.addWeighted(img, 0.75, watermark, 0.25, 0)
cv2.imshow("Watermarked image", out); cv2.imwrite("watermarked.jpg", out)
cv2.waitKey(0); cv2.destroyAllWindows()
