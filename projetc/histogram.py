import cv2
import numpy as np
import rtde_control
import rtde_io
import time

rtde_io_ = rtde_io.RTDEIOInterface("10.224.2.69")
rtde_c = rtde_control.RTDEControlInterface("10.224.2.69")

# Função para calcular o histograma
def calculate_histogram(image):
    # Converter a imagem para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calcular o histograma
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    # Normalizar o histograma
    hist /= hist.sum()
    return hist

# Função para comparar histogramas
def compare_histograms(hist1, hist2):
    # Calcular a correlação entre os dois histogramas
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return correlation

# Capturar vídeo da câmera
cap = cv2.VideoCapture(0)

# Carregar a imagem de referência
reference_image_red = cv2.imread('projetc/vermelho_foto.jpeg')

 # Carregar a imagem de referência
reference_image_red = cv2.imread('vermelho_foto.jpeg')

reference_hist_red = calculate_histogram(reference_image_red)

reference_image_black = cv2.imread('projetc/preto_foto.jpeg')
reference_hist_black = calculate_histogram(reference_image_black)


while True:
        # Capturar frame a frame
    ret, frame = cap.read()

    # Calcular o histograma do frame em tempo real
    real_time_hist = calculate_histogram(frame)

    
    # Comparar o histograma em tempo real com o histograma de referência
    if compare_histograms(real_time_hist, reference_hist_red) >= 0.75:
        cv2.putText(frame, 'Histograms Match!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  # vermelho
    
        base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]
        bef_a1 =  [-2.9020732084857386, -1.077377275829651, 1.804741684590475, -2.3604818783202113, -1.5067532698260706, -2.5751686731921595] 
        a1 =  [-2.9105411211596888, -0.9263118666461487, 1.8049700895892542, -2.4291798077025355, -1.5006964842425745, -2.5751927534686487]
        rtde_c.moveJ(bef_a1)
        rtde_c.moveJ(a1)
        rtde_c.moveJ(base)
        rtde_c.moveJ(bef_a1)
        rtde_c.moveJ(a1)
        rtde_c.moveJ(base)    


    if compare_histograms(real_time_hist,reference_hist_black) >= 0.77:
        cv2.putText(frame, 'Histograms Match!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2) # preto

        base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]
        a = [-4.076599899922506, -0.7863095563701172, 1.3410056273089808, -2.090026994744772, -1.4898093382464808, -2.235628906880514, 5] 
        rtde_c.moveJ(a)
        rtde_c.moveJ(base)
        rtde_c.moveJ(a)
        rtde_c.moveJ(base)

    
    # Mostrar o frame
    cv2.imshow('Real-time Histogram Comparison', frame)

    # Sair do loop se 'q' for pressionado
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
