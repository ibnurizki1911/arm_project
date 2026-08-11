import numpy as np

class arm :

    def __init__(self,name):
        self.name = name

    def Rz(self,theta):
        c = np.cos(theta)
        s = np.sin(theta)

        return np.array([
            [c,-s,0,0],
            [s, c,0,0],
            [0, 0,1,0],
            [0, 0,0,1]

        ])
    def Rx(self,theta):
        c = np.cos(theta)
        s = np.sin(theta)
        return np.array([
            [1,0, 0,0],
            [0,c,-s,0],
            [0,s, c,0],
            [0,0, 0,1]

        ])
    
    def Ry(self,theta):
        c = np.cos(theta)
        s = np.sin(theta)
        return np.array([
            [ c,0,s,0],
            [ 0,1,0,0],
            [-s,0,c,0],
            [ 0,0,0,1]
        ])
    
    def transX(self,a):
        P = np.array([a,0,0])
        T = np.eye(4)
        T[:3,3] = P

        return T
    
    def transZ(self,d):
        P = np.array([0,0,d])
        T = np.eye(4)
        T[:3,3] = P
        
        return T

    def fk_dh(self,rz,d,a,alpa):
        DH = (self.Rz(rz)@ self.transZ(d)
              @ self.transX(a)@ self.Rx(alpa))
        
        return DH


