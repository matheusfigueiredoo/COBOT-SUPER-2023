import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
    # Calcula o histograma da imagem em escala de cinza
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    # Plota o histograma
    plt.plot(histogram, color='gray')
    plt.xlabel('Níveis de Cinza')
    plt.ylabel('Número de Pixels')
    plt.title('Histograma em Escala de Cinza')
    plt.show()

def main():
    # Carrega a imagem
    image = cv2.imread('foto_webcam_red.jpg')

    # Converte a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mostra a imagem em escala de cinza
    cv2.imshow('Imagem em Escala de Cinza', gray_image)
    cv2.waitKey(0)
    
    # Plota o histograma da imagem em escala de cinza
    plot_histogram(gray_image)

    # Fecha todas as janelas
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()