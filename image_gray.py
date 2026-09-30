import cv2

# Read the image
image = cv2.imread("download.jpg")

# Check whether image was loaded
if image is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display original image
cv2.imshow("Original Image", image)

# Display grayscale image
cv2.imshow("Grayscale Image", gray_image)

# Wait for a key
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()