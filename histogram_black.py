import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram, color='gray')
    plt.xlabel('Gray level')
    plt.ylabel('Pixels')
    plt.title('Histogram in Gray Scale')
    plt.show()

def main():
    image = cv2.imread('project/foto_webcam_black.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Image', gray_image)
    cv2.waitKey(0)
    plot_histogram(gray_image)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
