import cv2
import numpy as np

# Função para calcular o histograma
def calculate_histogram(image):
    # Converte a imagem para grayscale para criar a máscara
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplica a limiarização de Otsu para criar uma máscara
    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    # Calcular os histogramas para cada canal de cores
    histogram_R = cv2.calcHist([image], [0], None, [256], [0, 256])
    histogram_G = cv2.calcHist([image], [1], None, [256], [0, 256])
    histogram_B = cv2.calcHist([image], [2], None, [256], [0, 256])
    
    # Normaliza cada histograma
    histogram_R = cv2.normalize(histogram_R, histogram_R)
    histogram_G = cv2.normalize(histogram_G, histogram_G)
    histogram_B = cv2.normalize(histogram_B, histogram_B)

    # Concatena os histogramas
    histogram = np.concatenate((histogram_R, histogram_G, histogram_B))
    
    return histogram

# Função para comparar histogramas
def compare_histograms(hist1, hist2, threshold=0.9):
    # Calcular a correlação entre os dois histogramas
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    
    return correlation >= threshold

# Capturar vídeo da câmera
cap = cv2.VideoCapture(0)

# Carregar a imagem de referência
reference_image_red = cv2.imread('vermelho_foto.jpeg')
reference_hist_red = calculate_histogram(reference_image_red)

reference_image_black = cv2.imread('ReferenciaPreto.jpg')
reference_hist_black = calculate_histogram(reference_image_black)

while True:
    # Capturar frame a frame
    ret, frame = cap.read()

    # Calcular o histograma do frame em tempo real
    real_time_hist = calculate_histogram(frame)

    # Comparar o histograma em tempo real com o histograma de referência
    if compare_histograms(real_time_hist, reference_hist_red):
        cv2.putText(frame, 'Histograms Match!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print('Cor vermelha detectada')

    if compare_histograms(real_time_hist,reference_hist_black):
        cv2.putText(frame, 'Histograms Match!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print('Cor preta detectada')

    # Mostrar o frame
    cv2.imshow('Real-time Histogram Comparison', frame)

    # Sair do loop se 'q' for pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a captura e fechar todas as janelas
cap.release()
cv2.destroyAllWindows()