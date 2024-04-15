# teste com orientacao a objeetos

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

time.sleep(0)

# movimentos para a peca vermelha
class move_red:
    def __init__(self, count):
        self.count = count
        if count == 1:
            rtde_c.moveJ(red_1)
        elif count == 2:
            rtde_c.moveJ(red_2)
        elif count == 3:
            rtde_c.moveJ(red_3)
        elif count == 4:
            rtde_c.moveJ(red_4)
        elif count == 5:
            rtde_c.moveJ(red_5)
        elif count == 6:
            rtde_c.moveJ(red_6)
        else:
            rtde_c.moveJ(pos_initial)

# movimentos para a peca preta
class black_box:
    def __init__(self, count):
        self.count = count

    def move_black(self, count):
        if self.count == 1:
            rtde_c.moveJ(black_1)
        elif self.count == 2:
            rtde_c.moveJ(black_2)
        elif self.count == 3:
            rtde_c.moveJ(black_3)
        elif self.count == 4:
            rtde_c.moveJ(black_4)
        elif self.count == 5:
            rtde_c.moveJ(black_5)
        elif self.count == 6:
            rtde_c.moveJ(black_6)
        else:
            rtde_c.moveJ(pos_initial)


# deteccao de pecas
memory_red = 0
memory_black = 0


black = black_box(memory_black)


# peca detectada

# vermelha 


