import cv2
import numpy as np

def detect_colors(image):
    # Convertendo a imagem para o espaço de cores HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Definindo os intervalos de cor para vermelho e preto
    lower_red = np.array([0, 100, 100])  # Limite inferior para a cor vermelha
    upper_red = np.array([10, 255, 255])  # Limite superior para a cor vermelha
    
    lower_black = np.array([0, 0, 0])  # Limite inferior para a cor preta
    upper_black = np.array([180, 255, 30])  # Limite superior para a cor preta

    # Criando máscaras para as cores vermelha e preta
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_black = cv2.inRange(hsv_image, lower_black, upper_black)

    # Encontrando contornos na máscara
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_black, _ = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhando contornos na imagem original
    image_with_contours_red = image.copy()
    image_with_contours_black = image.copy()

    cv2.drawContours(image_with_contours_red, contours_red, -1, (0, 0, 255), 2)
    cv2.drawContours(image_with_contours_black, contours_black, -1, (0, 0, 0), 2)

    return image_with_contours_red, image_with_contours_black

# Captura de vídeo da webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Chamando a função para detectar as cores vermelha e preta
    frame_red, frame_black = detect_colors(frame)

    # Exibindo as imagens
    cv2.imshow("Red Objects", frame_red)
    cv2.imshow("Black Objects", frame_black)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberando a captura de vídeo e fechando as janelas
video.release()
cv2.destroyAllWindows()