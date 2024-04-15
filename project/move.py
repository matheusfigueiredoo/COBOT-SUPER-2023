import rtde_control
import rtde_io
import time

HOST = "10.224.2.60"

rtde_io_ = rtde_io.RTDEIOInterface(HOST)
rtde_c = rtde_control.RTDEControlInterface(HOST)

# positions
pos_pick =  [-1.0761974493609827, -0.6395256084254761, 2.1842520872699183, -3.5842048130431117, -1.500361744557516, 0.7962992787361145]
pos_ref_pick = [-1.0243995825396937, -1.3618595165065308, 2.115596596394674, -2.3239323101439417, -1.5665572325335901, 0.779410719871521]
pos_ref_base = []

ref_red_1 = [-0.6810215155230921, -1.0891356629184266, 1.866720978413717, -2.3163911304869593, -1.498359505330221, 1.0935126543045044]
red_1 = [-0.663513485585348, -0.9728068274310608, 1.8943570295916956, -2.453865190545553, -1.5390127340899866, 1.0568325519561768]

ref_red_2 = [-0.5179546515094202, -0.992003397350647, 1.7566660086261194, -2.2961398563780726, -1.5611174742328089, 1.2233943939208984]
red_2 = [-0.5120299498187464, -0.9109321993640442, 1.7561996618853968, -2.359763284722799, -1.5613582769977015, 1.2234282493591309]

ref_red_3 =  [-0.6820767561541956, -0.8801615399173279, 1.540309254323141, -2.165537496606344, -1.5360353628741663, 1.2144827842712402]
red_3 =  [-0.6811183134662073, -0.8064618867686768, 1.5420931021319788, -2.2319804630675257, -1.5370672384845179, 1.2148873805999756]

ref_red_4 = [-0.5843132177935999, -0.8571840089610596, 1.5078581015216272, -2.23540796856069, -1.494725529347555, 1.2172341346740723]
red_4 = [-0.5848763624774378, -0.7785723370364686, 1.508374039326803, -2.288527627984518, -1.4947503248797815, 1.2172349691390991]

ref_red_5 = [-0.7163346449481409, -0.7167601150325318, 1.2113569418536585, -2.028078695336813, -1.4950240294085901, 1.204655647277832]
red_5 = [-0.714203182850973, -0.6396339696696778, 1.2129514853106897, -2.1050898037352503, -1.4949167410479944, 1.204654335975647]

ref_red_6 = [-0.6101377646075647, -0.6600688856891175, 1.1176837126361292, -2.0204316578307093, -1.4944513479815882, 1.2086352109909058]
red_6 = [-0.6207187811480921, -0.5910507601550599, 1.1177695433246058, -2.0644809208311976, -1.4715197722064417, 1.2085601091384888]


ref_black_1 = []
black_1 = []

ref_black_2 = []
black_2 = []

ref_black_3 = []
black_3 = []

ref_black_4 = []
black_4 = []

ref_black_5 = []
black_5 = []

ref_black_6 = []
black_6 = []


# pecas vermelhas
# memory red eh a variavel que conta as pecas armazenadas

def to_red(memory_red):
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
    
    if memory_red == 6:
        memory_red = 0
    
    return memory_red

# pecas pretas
# memory black eh a variavel que conta as pecas armazenadas

def to_black(memory_black):
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

    if memory_black == 6:
        memory_black = 0
    
    return memory_black