import cv2
import numpy as np

# Função para detectar a cor vermelha
def detect_red_color(frame):
    # Defina os limites inferior e superior para a cor vermelha na escala BGR
    lower_red = np.array([0, 0, 100])
    upper_red = np.array([100, 100, 255])

    # Converta o frame para o espaço de cores HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Crie uma máscara para a cor vermelha
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)

    # Encontre os contornos na máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Verifique se há contornos e imprima a mensagem se a cor vermelha for detectada
    if contours:
        print("Cor detectada")
        return True
    return False

# Inicie a captura de vídeo da câmera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame a frame
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensione o frame para melhor visualização
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    # Detecte a cor vermelha
    if detect_red_color(frame):
        pass  # Continue o loop se a cor vermelha for detectada

    # Mostre o frame
    cv2.imshow('Camera', frame)

    # Verifique se a tecla 'q' é pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere os recursos
cap.release()
cv2.destroyAllWindows()
