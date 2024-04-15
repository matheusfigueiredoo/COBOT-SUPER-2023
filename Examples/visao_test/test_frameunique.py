# import cv2
 
# img = cv2.imread("g.png", cv2.IMREAD_COLOR)
 
# cv2.imshow("guido", img)
 
# cv2.waitKey(0)
 
# cv2.destroyAllWindows()
import cv2
import rtde_control
import time

rtde_c = rtde_control.RTDEControlInterface("123")

base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]
a = [-2.9020732084857386, -1.077377275829651, 1.804741684590475, -2.3604818783202113, -1.5067532698260706, -2.5751686731921595]
b = [-2.9105411211596888, -0.9263118666461487, 1.8049700895892542, -2.4291798077025355, -1.5006964842425745, -2.5751927534686487]

c = [-5.1198371092425745, -1.3571563524058838, 2.360985342656271, -2.586445470849508, -1.5682628790484827, -2.1495588461505335]
d = [-5.1198371092425745, -1.0004556340030213, 2.360985342656271, -2.586445470849508, -1.5682628790484827, -2.1495588461505335]


x = True

while x :

    webcam = cv2.VideoCapture(0)

    if webcam.isOpened():
        validacao, frame = webcam.read()
        while validacao:
            validacao, frame = webcam.read()
            cv2.imshow("Video da Webcam", frame)
            key = cv2.waitKey(5)
            if key == 27: # ESC
                
                cv2.imwrite("peca.png", frame)
                img = cv2.imread("peca.png", cv2.IMREAD_COLOR)
                cv2.imshow("peca.png", img)
                break

            if key == ord("q"):
                break            

    webcam.release()
    cv2.destroyAllWindows()

    # moviments
    rtde_c.moveJ(base)
    rtde_c.moveJ(a)
    rtde_c.moveJ(b)







