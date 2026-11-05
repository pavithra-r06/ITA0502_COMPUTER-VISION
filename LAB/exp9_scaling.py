import cv2

# Read the image
image = cv2.imread("download.jpg")

# Get original size
height, width = image.shape[:2]

# Resize to bigger size
bigger = cv2.resize(image, (width * 2, height * 2))

# Resize to smaller size
smaller = cv2.resize(image, (width // 2, height // 2))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()