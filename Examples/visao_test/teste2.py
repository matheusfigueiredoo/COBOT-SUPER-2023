import numpy as np
import cv2

# Define os ranges da cor
colors = {
    "red": ((0, 100, 100), (10, 255, 255)),
    "black": ((0, 0, 0), (180, 255, 255)),
    "blue": ((100, 100, 0), (120, 255, 255))
}

# Abre a webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura o frame
    ret, frame = cap.read()

    # Converte para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Loop para detectar a cor
    for color_name, color_range in colors.items():
        # Cria máscara para a cor
        mask = cv2.inRange(hsv, color_range[0], color_range[1])

        # Encontra os contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Desenha contornos
        if contours:
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Calcula a cor média
                mean_color = cv2.mean(frame, mask=mask)[0]

                # Mostra a cor média no terminal
                print("Cor média:", mean_color)

                # Mostra o nome da cor
                cv2.putText(frame, color_name.upper(), (10, 20 + (list(colors.keys()).index(color_name) * 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Tela de exibição de cor
    cv2.imshow("Color Detection", frame)

    # Sair do loop pressionando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()