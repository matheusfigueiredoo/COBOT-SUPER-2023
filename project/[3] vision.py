import cv2
import numpy as np
import time



# Função para calcular o histograma
def calculate_histogram(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist /= hist.sum()
    return hist

def calculate_histogram1(image):
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

# Função para mover para uma posição específica
def move_to_position(position):
    global em_execucao
    em_execucao = True

    time.sleep(1)

    em_execucao = False

# Função para comparar histogramas
def compare_histograms(hist1, hist2):
    # Calcular a correlação entre os dois histogramas
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return correlation

# Função principal
def main():
    # Capturar vídeo da câmera
    cap = cv2.VideoCapture(0)

    # Carregar imagens de referência e calcular histogramas
    reference_image_red = cv2.imread('foto_webcam_red.jpg')
    reference_hist_red = calculate_histogram1(reference_image_red)

    reference_image_black = cv2.imread('foto_webcam_black.jpg')
    reference_hist_black = calculate_histogram1(reference_image_black)

    while True:
        # Capturar frame a frame
        ret, frame = cap.read()

        # Calcular o histograma do frame em tempo real
        real_time_hist = calculate_histogram1(frame)

        # Comparar histogramas
        if compare_histograms(real_time_hist, reference_hist_red) >= 0.5:
            print('vermelho')
            cv2.putText(frame, 'Histograms Match!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # vermelho
            move_to_position([-2.9105411211596888, -0.9263118666461487, 1.8049700895892542, -2.4291798077025355, -1.5006964842425745, -2.5751927534686487])

        elif compare_histograms(real_time_hist, reference_hist_black) >= 0.5:
            print('preta')
            cv2.putText(frame, 'Histograms Match!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # preto
            move_to_position([-4.076599899922506, -0.7863095563701172, 1.3410056273089808, -2.090026994744772, -1.4898093382464808, -2.235628906880514])

        print(f'Comparação vermelho: {compare_histograms(real_time_hist, reference_hist_red)}')
        #print(f'Comparação preto: {compare_histograms(real_time_hist, reference_hist_black)}')

        # Exibir o frame
        cv2.imshow('Real-time Histogram Comparison', frame)

        # Esperar por uma tecla pressionada
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar a câmera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()  