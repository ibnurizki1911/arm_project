import numpy as np 
import matplotlib.pyplot as plt
from object_ARM import arm
import frame as fr

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_zlim(-100,100)

theta = 0
theta1 = 60
theta2 = 0
theta3 = 0
theta4 = -90
theta5 = 0
# ============control=============
def on_key(event):
    speed = 5
    global theta,theta1,theta2,theta3,theta4,theta5
    if event.key == 'w':
        theta += speed
    if event.key == 'e':
        theta -= speed
    if event.key == 'a':
        theta1 += speed
    if event.key == 'd':
        theta1 -= speed
    if event.key == 'x':
        theta2 += speed
    if event.key == 'z':
        theta2 -= speed
    if event.key == 'u':
        theta3 += speed
    if event.key == 'o':
        theta3 -= speed
    if event.key == 'l':
        theta4 += speed
    if event.key == 'k':
        theta4 -= speed
    if event.key == 'b':
        theta5 += speed
    if event.key == 'm':
        theta5 -= speed
        

fig.canvas.mpl_connect(
    'key_press_event',
    on_key
)

# ==============setup============
frame0 = fr.build_frame(ax)
frame1 = fr.build_frame(ax)
frame2 = fr.build_frame(ax)
frame3 = fr.build_frame(ax)
frame4 = fr.build_frame(ax)
frame5 = fr.build_frame(ax)
frame6 = fr.build_frame(ax)

link0 = fr.build_link(ax)
link1 = fr.build_link(ax)
link2 = fr.build_link(ax)
link3 = fr.build_link(ax)
link4 = fr.build_link(ax)
link5 = fr.build_link(ax)


arm1 = arm('lengan')

# ===========lopping==============


while plt.fignum_exists(fig.number):

    T0 = np.eye(4)
    T1 = arm1.fk_dh(np.radians(theta),10,0,np.radians(90))
    T12 = arm1.fk_dh(np.radians(theta1),0,80,np.radians(0))
    T23 = arm1.fk_dh(np.radians(theta2),5,0,np.radians(90))
    T34 = arm1.fk_dh(np.radians(theta3),60,0,np.radians(90))                              
    T45 = arm1.fk_dh(np.radians(theta4),5,0,np.radians(90))
    T56 = arm1.fk_dh(np.radians(theta5),20,0,np.radians(0))

    T02 = T1 @ T12
    T03 = T02 @ T23
    T04 = T03 @ T34
    T05 = T04 @ T45
    T06 = T05 @ T56


    fr.update_frame(T0,frame0)
    # fr.update_frame(T1,frame1)
    # fr.update_frame(T02,frame2)
    # fr.update_frame(T03,frame3)
    # fr.update_frame(T04,frame4)
    # fr.update_frame(T05,frame5)
    fr.update_frame(T06,frame6)

    fr.update_link(T0,T1,link0)
    fr.update_link(T1,T02,link1)
    fr.update_link(T02,T03,link2)
    fr.update_link(T03,T04,link3)
    fr.update_link(T04,T05,link4)
    fr.update_link(T05,T06,link5)
        
    plt.pause(0.01)
