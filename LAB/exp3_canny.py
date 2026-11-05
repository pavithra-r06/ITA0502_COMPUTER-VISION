import cv2

image = cv2.imread("download.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", image)
cv2.imshow("Outline", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()