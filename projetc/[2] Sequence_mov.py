import rtde_control
import rtde_io
import time

HOST = "123"

rtde_io_ = rtde_io.RTDEIOInterface(HOST)
rtde_c = rtde_control.RTDEControlInterface(HOST)

# positions
pos_initial = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]

red_1 = []
red_2 = []
red_3 = []
red_4 = []
red_5 = []
red_6 = []

black_1 = []
black_2 = []
black_3 = []
black_4 = []
black_5 = []
black_6 = []


# moviments sequency
rtde_c.moveJ(pos_initial)
time.sleep(1)

# manter a garra na posicao inicial
rtde_io_.setToolDigitalOut(1, False)
rtde_io_.setToolDigitalOut(0, True)

# sequencia dos movimentos de acordo com a chegada 
# das pecas

# pecas vermelhas
# place red eh a variavel que conta as pecas armazenadas

place_red = 0


if place_red == 0:
    rtde_c.moveJ(red_1)
    place_red = place_red + 1

if place_red == 1:
    rtde_c.moveJ(red_2)
    place_red = place_red + 1 

if place_red == 2:
    rtde_c.moveJ(red_3)
    place_red = place_red + 1 

if place_red == 3:
    rtde_c.moveJ(red_4)
    place_red = place_red + 1

if place_red == 4:
    rtde_c.moveJ(red_5)
    place_red = place_red + 1

if place_red == 5:
    rtde_c.moveJ(red_6)
    place_red = place_red + 1