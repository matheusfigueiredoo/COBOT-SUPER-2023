import cv2
import numpy as np
import time
import teste_move 

# histograma
def calculate_histogram(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist /= hist.sum()
    return hist


def calculate_histogram1(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    histogram_R = cv2.calcHist([image], [0], mask, [256], [0, 256])
    histogram_G = cv2.calcHist([image], [1], mask, [256], [0, 256])
    histogram_B = cv2.calcHist([image], [2], mask, [256], [0, 256])
    
    histogram_R = cv2.normalize(histogram_R, histogram_R)
    histogram_G = cv2.normalize(histogram_G, histogram_G)
    histogram_B = cv2.normalize(histogram_B, histogram_B)

    histogram = np.concatenate((histogram_R, histogram_G, histogram_B))
    
    return histogram


# comparacao histogramas
def compare_histograms(hist1, hist2):
    correlation = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return correlation

def crop_image(frame, x, y, width, height): # recorte da imagem
    cropped_frame = frame[y:y+height, x:x+width] 
    return cropped_frame

x, y, width, height = 100, 100, 150, 150  


def main():
    cap = cv2.VideoCapture(0)
    reference_image_red = cv2.imread('foto_webcam_red.jpg')
    reference_hist_red = calculate_histogram(reference_image_red)

    reference_image_black = cv2.imread('foto_webcam_black.jpg')
    reference_hist_black = calculate_histogram(reference_image_black)

    memory_red = 0
    memory_black = 0

    while True:
        ret, frame = cap.read()
        cropped_frame = crop_image(frame, x, y, width, height)
        real_time_hist = calculate_histogram(cropped_frame)

        if compare_histograms(real_time_hist, reference_hist_red) >= 0.88:
            print('vermelha')
            teste_move.move_red_piece(memory_red)
            memory_red += 1
            

        elif compare_histograms(real_time_hist, reference_hist_black) >= 0.85:
            print('preta')
            teste_move.move_black_piece(memory_black)
            memory_black += 1
        #print(f'Comparação vermelho: {compare_histograms(real_time_hist, reference_hist_red)}')
        #print(f'Comparação preto: {compare_histograms(real_time_hist, reference_hist_black)}')

        cv2.imshow('Real-time Histogram Comparison', cropped_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
