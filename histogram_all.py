import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image, color):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram, color=color)

def main():
    image1 = cv2.imread('project/foto_webcam_black.jpg', cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread('project/foto_webcam_red.jpg', cv2.IMREAD_GRAYSCALE)
    image3 = cv2.imread('project/foto_webcam_nothing.jpg', cv2.IMREAD_GRAYSCALE)

    plt.figure(figsize=(10, 5))
    plot_histogram(image1, 'blue')
    plot_histogram(image2, 'green')
    plot_histogram(image3, 'red')

    plt.xlabel('Gray level')
    plt.ylabel('Pixels')
    plt.title('Histogram')
    plt.legend(['Black', 'Red', 'Nothing'])
    plt.show()

if __name__ == "__main__":
    main()
