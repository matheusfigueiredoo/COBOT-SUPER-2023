import histogram
import move_robo 
import rtde_control
import rtde_io
import time

rtde_io_ = rtde_io.RTDEIOInterface("10.224.2.69")
rtde_c = rtde_control.RTDEControlInterface("10.224.2.69")




cor = histogram.mostra_cor()

    

if cor == "000":
    bef_a1 =  [-2.9020732084857386, -1.077377275829651, 1.804741684590475, -2.3604818783202113, -1.5067532698260706, -2.5751686731921595] 
    a1 =  [-2.9105411211596888, -0.9263118666461487, 1.8049700895892542, -2.4291798077025355, -1.5006964842425745, -2.5751927534686487]
    rtde_c.moveJ(bef_a1)
    rtde_c.moveJ(a1)
            
    
    

