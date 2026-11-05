import cv2, sys
# Template matching: provide the scene image and a cropped watch template.
if len(sys.argv) < 3:
    raise SystemExit("Usage: python 25_watch_object_recognition.py scene.jpg watch_template.jpg")
img = cv2.imread(sys.argv[1]); template = cv2.imread(sys.argv[2])
if img is None or template is None: raise SystemExit("Could not read scene or template image.")
gray, templ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
th, tw = templ.shape[:2]
if th > gray.shape[0] or tw > gray.shape[1]: raise SystemExit("Template must be smaller than scene.")
result = cv2.matchTemplate(gray, templ, cv2.TM_CCOEFF_NORMED)
_, score, _, location = cv2.minMaxLoc(result)
bottom_right = (location[0] + tw, location[1] + th)
out = img.copy()
cv2.rectangle(out, location, bottom_right, (0,255,0), 2)
cv2.putText(out, f"Watch match: {score:.2f}", (location[0], max(25,location[1]-10)),
            cv2.FONT_HERSHEY_SIMPLEX, .7, (0,255,0), 2)
cv2.imshow("Watch recognition", out); cv2.imwrite("watch_detection.jpg", out)
cv2.waitKey(0); cv2.destroyAllWindows()
