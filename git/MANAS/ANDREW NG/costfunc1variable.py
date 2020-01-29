import numpy as np
import matplotlib.pyplot as py
a = np.genfromtxt('ex1data1.txt', dtype=float, delimiter=',')
x=a[0:,0]
y=a[0:,1]
n1=float(input('give value of theta1'))
n2=float(input('give value of theta2'))
theta = [n1,n2] 
def computeCost(x,y,theta):
    m=y.shape[0]
    s=0
    for i in range(0,m):
        s=(((theta[0]+theta[1]*x[i])-y[i])**2)+s
    P = s*(1/(2*m))
    return P
P = computeCost(x,y,theta)