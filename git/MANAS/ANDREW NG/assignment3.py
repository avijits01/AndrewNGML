import numpy as np
import matplotlib.pyplot as py
a = np.genfromtxt('ex2data1.txt', dtype=float, delimiter=',')
y=a[:,2:3]
x=a[:,0:2]
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.dot(X, theta)
h = sigmoid(z)
def cost(theta,x,y):
    m=len(y)
    one=np.ones(m)
    one=one.reshape(m,1)
    print(one.shape)
    x=np.hstack((one,x))
    p=x.dot(theta)
    c=np.sum(np.square(p)-y)
    return c
def loss(x, y,theta):
    m=len(y)
    one=np.ones(m)
    one=one.reshape(m,1)
    x=np.hstack((one,x))
    z=np.dot(x,theta)
    h=sigmoid(z)
    c= np.sum((-y.transpose() * np.log(h) - (1 - y).transpose() * np.log(1 - h)))/m
    return c
def grad(x,y,theta,a,itern):
    m=len(y)
    one=np.ones(m)
    one=one.reshape(m,1)
    x=np.hstack((one,x))
    z=np.dot(x,theta.reshape(3,1))
    h=sigmoid(z)
    for i in range(0,itern):
        gradient = np.dot(x.transpose(), (h - y))
        gradient=gradient.reshape(1,3)
        theta = theta-(gradient*(a/m))
    return theta    
t=grad(x,y,theta=np.array([[-24,0.2,0.2]]),a=0.001,itern=1000)

