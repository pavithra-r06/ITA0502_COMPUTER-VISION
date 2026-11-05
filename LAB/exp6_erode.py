import cv2
import numpy as np

# Read the image
image = cv2.imread("download.jpg")

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()