import cv2

image = cv2.imread("download.jpg")

if image is None:
    print("Image not found!")
    exit()

blur_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur Image", blur_image)

cv2.waitKey(0)
cv2.destroyAllWindows()