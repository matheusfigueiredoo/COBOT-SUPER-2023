import cv2
import numpy as np

# taking the input from webcam
vid = cv2.VideoCapture(0)

# running while loop just to make sure that
# our program keep running until we stop it
while True:

# capturing the current frame
    _   ,frame = vid.read()

# displaying the current frame
    cv2.imshow("frame", frame)

# setting values for base colors
    r = frame[:, :, 2:]
    g = frame[:, :, 1:2]
    b = frame[:, :, :1]

    # computing the mean
    r_mean = np.mean(r)
    g_mean = np.mean(g)
    b_mean = np.mean(b)

    # displaying the most prominent color
    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > r_mean and g_mean > b_mean):
        print("Green")
    else:
        print("Red")





        