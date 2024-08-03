import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a blank image
img = np.zeros((200, 200), dtype=np.uint8)

# Draw a circle
cv2.circle(img, (100, 100), 50, 255, -1)

# Use Canny edge detector to find edges
edges = cv2.Canny(img, 50, 150)

# Detect circles using Hough Transform
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.0, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=100)

# Draw the circles on the image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, 127, 1)
        cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), 255, -1)

# Display the result
plt.imshow(img, cmap='gray')
plt.title('Detected Circle')
plt.show()