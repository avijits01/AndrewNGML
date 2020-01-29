import numpy as np
import matplotlib.pyplot as py
a = np.genfromtxt('ex1data2.txt',dtype=float,delimiter=',')
x=a[:,0:2]
y=a[:,2:3]
m=x.shape[0]
one = np.ones(m)
x=np.hstack((one,x))
theta=np.array([1,1,1])
theta.reshape(3,1)
def multicostf(x):
    s=0
    h= lambda x: x.reshape(1,3).dot(theta)
    for i in range (0,m):
        s=(h(x[i])-y[i])**2+s
    return ((1/(2*m))*s)        
      

