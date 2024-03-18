import cv2
import numpy as np

def calculate_histogram(image):
    # Converte a imagem para grayscale para criar a máscara
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplica a limiarização de Otsu para criar uma máscara
    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # Calcular os histogramas para cada canal de cores
    histogram_R = cv2.calcHist([image], [0], mask, [256], [0, 256])
    histogram_G = cv2.calcHist([image], [1], mask, [256], [0, 256])
    histogram_B = cv2.calcHist([image], [2], mask, [256], [0, 256])
    
    # Normaliza cada histograma
    histogram_R = cv2.normalize(histogram_R, histogram_R)
    histogram_G = cv2.normalize(histogram_G, histogram_G)
    histogram_B = cv2.normalize(histogram_B, histogram_B)

    # Concatena os histogramas
    histogram = np.concatenate((histogram_R, histogram_G, histogram_B))
    
    return histogram

# Função para comparar histogramas
def compare_histograms(hist1, hist2):
    # Calcular a correlação entre os dois histogramas
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYY)
    
    return correlation

# Carregar a imagem de referência

reference_image_black = cv2.imread('ReferenciaPreto.jpg')
reference_hist_black = calculate_histogram(reference_image_black)

# Capturar vídeo da câmera
cap = cv2.VideoCapture(0)




while True:
    # Capturar frame a frame
    ret, frame = cap.read()

    # Calcular o histograma do frame em tempo real
    real_time_hist = calculate_histogram(frame)


    x = compare_histograms(real_time_hist,reference_hist_black)
    
    print(x)

    # Mostrar o frame
    cv2.imshow('Real-time Histogram Comparison', frame)

    # Sair do loop se 'q' for pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   


# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()