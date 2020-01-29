import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
a = np.genfromtxt('ex1data2.txt',dtype=float,delimiter=',')
x=a[:,0:2]
y=a[:,2:3]
def loss(theta,x,y):
    theta=theta.reshape(1,3);
    z=np.dot(x,theta.T)
    h=sigmoid(z)
    c= np.sum((-y.transpose().dot(np.log(h)) - (1 - y).transpose().dot(np.log(1 - h))))/m
    grad = (np.sum((sigmoid(np.dot(x,theta.T))-y)*x,axis=0)/m)
    return (c,grad)
def predict(theta,x):
    p=sigmoid(np.dot(x,theta))
    m=p.size
    b=np.zeros(m)
    for i in range(0,m) :
        print(p[i])
        if(p[i]>0.5):
            b[i]=1
        else:
            b[i]=0
    return b        
loss(initial_theta,x,y)
res = minimize(loss,initial_theta,method='Newton-CG',args=(x,y),jac=True, options={'maxiter':400,'disp':True})
theta=res.x
p=predict(theta,x)
print('Train Accuracy: \n', np.mean(p==y1)*100)

