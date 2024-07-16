import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram, color='gray')
    plt.xlabel('Níveis de Cinza')
    plt.ylabel('Número de Pixels')
    plt.title('Histograma em Escala de Cinza')
    plt.show()

def main():
    image = cv2.imread('project/foto_webcam_red.jpg')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Imagem em Escala de Cinza', gray_image)
    cv2.waitKey(0)
    plot_histogram(gray_image)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
