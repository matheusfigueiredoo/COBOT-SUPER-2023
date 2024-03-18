import rtde_control
import rtde_io
import time

rtde_io_ = rtde_io.RTDEIOInterface("10.224.2.69")
rtde_c = rtde_control.RTDEControlInterface("10.224.2.69")


base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]

a = [-4.076599899922506, -0.7863095563701172, 1.3410056273089808, -2.090026994744772, -1.4898093382464808, -2.235628906880514, 5]

b = [-4.059603039418356, -0.7164358657649537, 1.383453671132223, -2.2590977154173792, -1.5111663977252405, -2.1496413389789026]

var = 1

# moviments sequency

rtde_c.moveJ(base)
time.sleep(1)
rtde_c.moveJ(a)
rtde_c.moveJ(b)
rtde_io_.setToolDigitalOut(1, True)
time.sleep(0.5)
rtde_c.moveJ(a)
rtde_c.moveJ(base)


# to place

bef_a1 =  [-2.9020732084857386, -1.077377275829651, 1.804741684590475, -2.3604818783202113, -1.5067532698260706, -2.5751686731921595] 
a1 =  [-2.9105411211596888, -0.9263118666461487, 1.8049700895892542, -2.4291798077025355, -1.5006964842425745, -2.5751927534686487]



rtde_c.moveJ(bef_a1)
rtde_c.moveJ(a1)
time.sleep(0.5)
rtde_io_.setToolDigitalOut(1, False)
rtde_io_.setToolDigitalOut(0, True)
time.sleep(0.5)
rtde_c.moveJ(bef_a1)
rtde_c.moveJ(base)
rtde_io_.setToolDigitalOut(0, False)