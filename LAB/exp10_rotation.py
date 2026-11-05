import cv2

# Read the image
image = cv2.imread("download.jpg")

# Rotate 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()