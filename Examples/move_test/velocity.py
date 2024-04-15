import rtde_control

rtde_c = rtde_control.RTDEControlInterface("10.224.2.69")

# Parameters
acceleration = 1
dt = 1.0/500  # 2ms
base = [-4.036092583333151, -1.3568094980767746, 2.373448912297384, -2.5869633160033167, -1.568237606679098, -2.1496198813067835]
point1 = [-0.014040295277730763, -2.5335470638670863, -1.375672459602356, -0.7301484507373353, 1.6832222938537598, 0.025106282904744148]

# Move to initial joint position with a regular moveJ
rtde_c.moveJ(base)
rtde_c.moveJ(point1)