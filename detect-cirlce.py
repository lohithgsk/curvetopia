import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_circle(image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise and improve circle detection
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)
    
    # Use Canny edge detector to find edges
    edges = cv2.Canny(blurred, 50, 150)
    
    # Detect circles using Hough Transform
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.0, minDist=20,
                               param1=50, param2=30, minRadius=10, maxRadius=100)
    
    # Draw the circles on the image
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 2)  # Draw the circle
            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)  # Draw the center
        
    # Display the result
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Detected Circle')
    plt.axis('off')
    plt.show()

# Path to your image file
image_path = 'C:/Lohith/psg/adobe-genai/.venv/circle.jpeg'
detect_circle(image_path)