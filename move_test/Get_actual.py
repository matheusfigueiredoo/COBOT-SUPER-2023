import rtde_receive
from gripper import Gripper

rtde_r = rtde_receive.RTDEReceiveInterface("10.224.2.75")
gripper = Gripper("10.224.1.254")

actual_q = rtde_r.getActualQ()
print(actual_q)

gripper.set_position(0)
gripper.set_position(50)

#posicoes
# pos_ini = [-1.6171444098102015, -2.5287392775165003, -1.009193245564596, -1.197681728993551, 1.615891456604004, -1.6434147993670862]