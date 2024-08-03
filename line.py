import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a blank image
img = np.zeros((200, 200), dtype=np.uint8)

# Draw a line
cv2.line(img, (50, 50), (150, 150), 255, 1)

# Use Canny edge detector to find edges
edges = cv2.Canny(img, 50, 150)

# Detect lines using Hough Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

# Draw the lines on the image
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), 127, 1)

# Display the result
plt.imshow(img, cmap='gray')
plt.title('Detected Line')
plt.show()