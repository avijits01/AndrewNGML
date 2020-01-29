import numpy as np
import matplotlib.pyplot as py
a = np.genfromtxt('ex1data2.txt',dtype=float,delimiter=',')
def normal(b,y):
    temp1=b.transpose().dot(b)
    theta=(np.linalg.inv(temp1).dot(b.transpose())).dot(y)
    print(theta)
    return theta
def normalisation(x):
    n=x.shape[1]
    m=x.shape[0]
    for i in range(0,n):
        mu=x[:,i].mean()
        sigma=np.std(x[:,i])
        for j in range(0,m): #m are number of training example
            x[j,i]=(x[j,i]-mu)/sigma   
    return x        
       
x=a[:,0:2]
y=a[:,2:3]
def gradm(x,y,theta,a,iterations):
    x=normalisation(x)
    theta =theta.reshape(3,1)
    m=x.shape[0]
    n=x.shape[1]
    one=np.ones(m)
    one=one.reshape(47,1)
    x=np.hstack((one,x))
    xt=x.transpose()
    print(x.shape)
    print(theta.shape)
    print(x)
    for i in range(0,iterations):
        s=0
        for j in range (0,m):
            h = np.dot(x[j],theta)
            s=((h-y[j])*x[j])+s
        s=s.reshape(3,1)    
        theta=theta-((s*a)/m)
    return theta  
