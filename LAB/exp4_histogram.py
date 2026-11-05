import cv2

# Read the image
image = cv2.imread("download.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Display original image
cv2.imshow("Original Image", gray)

# Display equalized image
cv2.imshow("Histogram Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()