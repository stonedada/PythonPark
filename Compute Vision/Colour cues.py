import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('lena.jpg')
print('img shape:',image.shape)
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges using the Canny edge detection algorithm
edges = cv2.Canny(gray, 100, 200)

# Perform a dilation operation on the edges to make them thicker
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)

# Find contours in the dilated edges image
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# For each contour, check if it meets certain criteria to be considered a face
faces = []
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    aspect_ratio = float(w) / h
    area = cv2.contourArea(contour)
    if aspect_ratio >= 0.5 and aspect_ratio <= 1.5 and area >= 500 and area <= 5000:
        faces.append((x, y, w, h))

# Draw a bounding box around each detected face
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with bounding boxes around detected faces
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
