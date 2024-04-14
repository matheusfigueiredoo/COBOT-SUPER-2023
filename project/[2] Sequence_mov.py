import rtde_control
import rtde_io
import time

HOST = "123"
memory_red = 0
memory_black = 0

rtde_io_ = rtde_io.RTDEIOInterface(HOST)
rtde_c = rtde_control.RTDEControlInterface(HOST)

# positions
pos_pick = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]
pos_ref_pick = []
pos_ref_base = []

ref_red_1 = []
ref_red_2 = []
ref_red_3 = []
ref_red_4 = []
ref_red_5 = []
ref_red_6 = []
red_1 = []
red_2 = []
red_3 = []
red_4 = []
red_5 = []
red_6 = []

ref_black_1 = []
ref_black_2 = []
ref_black_3 = []
ref_black_4 = []
ref_black_5 = []
ref_black_6 = []
black_1 = []
black_2 = []
black_3 = []
black_4 = []
black_5 = []
black_6 = []

# moviments sequency
time.sleep(1)

# manter a garra na posicao inicial
rtde_io_.setToolDigitalOut(1, False)
rtde_io_.setToolDigitalOut(0, True)

# sequencia dos movimentos de acordo com a chegada 
# das pecas

# pecas vermelhas
# memory red eh a variavel que conta as pecas armazenadas

if memory_red == 0:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_red_1)
    rtde_c.moveJ(red_1)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_red_1)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)

if memory_red == 1:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_red_2)
    rtde_c.moveJ(red_2)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_red_2)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_red == 2:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_red_3)
    rtde_c.moveJ(red_3)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_red_3)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_red == 3:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_red_4)
    rtde_c.moveJ(red_4)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_red_4)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_red == 4:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_red_5)
    rtde_c.moveJ(red_5)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_red_5)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_red == 5:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_red_6)
    rtde_c.moveJ(red_6)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_red_6)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
memory_red = memory_red + 1

# pecas pretas
# memory black eh a variavel que conta as pecas armazenadas

if memory_black == 0:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_black_1)
    rtde_c.moveJ(black_1)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_black_1)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)   

if memory_black == 1:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_black_2)
    rtde_c.moveJ(black_2)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_black_2)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)  

if memory_black == 2:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_black_3)
    rtde_c.moveJ(black_3)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_black_3)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_black == 3:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_black_4)
    rtde_c.moveJ(black_4)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_black_4)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_black == 4:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_black_5)
    rtde_c.moveJ(black_5)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_black_5)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
if memory_black == 5:
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_pick)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, True)
    time.sleep(1)
    rtde_c.moveJ(pos_ref_pick)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(ref_black_6)
    rtde_c.moveJ(black_6)
    time.sleep(1)
    rtde_io_.setToolDigitalOut(1, False)
    rtde_io_.setToolDigitalOut(0, True)
    time.sleep(1)
    rtde_c.moveJ(ref_black_6)
    rtde_c.moveJ(pos_ref_base)
    rtde_c.moveJ(pos_ref_pick)
    
memory_black = memory_black + 1