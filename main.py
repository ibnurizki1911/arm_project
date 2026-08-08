import numpy as np 
import matplotlib.pyplot as plt
from object_ARM import arm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(-100,100)

theta = 0


def on_key(event):
    global theta
    if event.key == 'w':
        theta += 1
    if event.key == 'e':
        theta -= 1

fig.canvas.mpl_connect(
    'key_press_event',
    on_key
)

def build_frame():
    x_line, = ax.plot([0,0],[0,0],[0,0], color='r')
    y_line, = ax.plot([0,0],[0,0],[0,0], color='g')
    z_line, = ax.plot([0,0],[0,0],[0,0], color='b')
    
    return x_line,y_line,z_line

def update_frame(T,frame):
    
    x_line,y_line,z_line = frame
    
    R = T[:3,:3]
    P = T[:3, 3]
    scale = 30
    
    x = R[:,0] * scale + P
    y = R[:,1] * scale + P
    z = R[:,2] * scale + P
    
    x_line.set_data([P[0],x[0]],[P[1],x[1]])
    x_line.set_3d_properties([P[2],x[2]])
    
    y_line.set_data([P[0],y[0]],[P[1],y[1]])
    y_line.set_3d_properties([P[2],y[2]])

    z_line.set_data([P[0],z[0]],[P[1],z[1]])
    z_line.set_3d_properties([P[2],z[2]])

# setup
frame0 = build_frame()
frame1 = build_frame()

arm1 = arm('lengan')




plt.show(block=False)
while True:

    T0 = np.eye(4)
    T1 = arm1.fk_dh(np.radians(theta),50,0,np.radians(90))
    update_frame(T0,frame0)
    update_frame(T1,frame1)
    
    plt.pause(0.001)
