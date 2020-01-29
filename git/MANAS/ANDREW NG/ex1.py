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
h = lambda x : theta[0]+x*theta[1]
def summ(x,y,theta):
    m=a.shape[0]
    s1=0
    s2=0
    for j in range(0,m):
                s1= (h(j)-y[j])+s1
                s2 = ((h(j)-y[j])*x[j])+s2
    return (1/m)*s1,(1/m)*s2        
def gradientDescent(x, y, theta, alpha, iterations):
    for i in range (0,iterations):
        temp = computeCost(x,y,theta)
        u,v= summ(x,y,theta)
        theta[0]=theta[0]-alpha*u
        theta[1]=theta[1]-alpha*v
        if(computeCost(x,y,theta)>temp):
            return theta
    return theta
t= gradientDescent(x, y, theta=[0,0], alpha=0.01, iterations=1000)
def my_line(x,t):
    return t[1] * (x) + t[0]
py.plot(x, my_line(x,t))
py.ylabel('Profit in $10,000s');
py.xlabel('Population of City in 10,000s')
py.plot(x,y,'bo')
x = int(input("input population"))
def predict(x):
    y = t[1]*x+t[0]
    return y
sol = predict(x)
print(sol) 