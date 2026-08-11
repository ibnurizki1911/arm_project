
def build_frame(ax):
    x_line, = ax.plot([],[],[], color='r')
    y_line, = ax.plot([],[],[], color='g')
    z_line, = ax.plot([],[],[], color='b')
    
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

def build_link(ax):
    link,=ax.plot([],[],[],color='black',linewidth=3)

    return link
def update_link(frame_in,frame_out,link):

    P_in = frame_in[:3,3]
    P_out = frame_out[:3,3]

    link.set_data(
        [P_in[0],P_out[0]],
        [P_in[1],P_out[1]]
    )
    link.set_3d_properties([P_in[2],P_out[2]])
