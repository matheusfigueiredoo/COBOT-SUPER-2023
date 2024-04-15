import numpy as np
import cv2

# Define OS rangers da cor
colors = {
    "red": ((0, 100, 100), (10, 255, 255)),
    "black": ((0, 0, 0), (180, 255, 255)),
    "blue": ((100, 100, 0), (120, 255, 255))
}

# Abre webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura o frame
    ret, frame = cap.read()

    # Converte pra hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Loop pra detectar a cor
    for color_name, color_range in colors.items():
        # Create mask for the color
        mask = cv2.inRange(hsv, color_range[0], color_range[1])

        # encontrar os contornos
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # desenhar contornos
        if contours:
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # calcular a coordenada y para posicionamento de texto 
                text_y = 20 if len(colors) == 1 else 20 + (list(colors.keys()).index(color_name) * 30)

                # mostra o nome da cor
                cv2.putText(frame, color_name.upper(), (10, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # tela de exibicao de cor
    cv2.imshow("Color Detection", frame)

    # sair do loop pressione q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()