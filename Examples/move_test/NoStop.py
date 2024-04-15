import rtde_control
import rtde_io
import time

rtde_io_ = rtde_io.RTDEIOInterface("10.224.2.69")
rtde_c = rtde_control.RTDEControlInterface("10.224.2.69")

base = [-4.295280639325277, -1.2305423480323334, 2.051667038594381, -5.551773925820822, 1.538703441619873, -2.5057719389544886]
a = [-3.4835787455188196, -0.29754896581683354, 0.7144029776202601, -5.202568670312399, 1.6166739463806152, -2.5057366530047815]
b = [-4.696701471005575, -0.1104920667460938, 0.38328773180116826, -5.019893547097677, 1.5992377996444702, -2.321280304585592]
last = [-1.54, -1.83, -2.28, -0.59, 1.60, 0.023]

# moviments sequency

#base to point b
rtde_c.moveJ(base)
rtde_c.moveJ(a)

# close the gripper
time.sleep(0.3)
rtde_io_.setToolDigitalOut(1, True)
#time.sleep(0.5)

# move to base and to the second point
rtde_c.moveJ(base)
rtde_c.moveJ(b)


rtde_c.moveJ(base)