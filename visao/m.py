import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # Capturar frame a frame
    ret, frame = cap.read()
    
   
    cv2.imshow('Real-time Histogram Comparison', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()