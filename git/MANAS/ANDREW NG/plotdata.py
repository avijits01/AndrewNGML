import numpy as np
import matplotlib.pyplot as py
def plotdata():
    a = np.genfromtxt('ex1data1.txt', dtype=float, delimiter=',')
    x= a[0:,0]
    y = a[0:,1]
    py.ylabel('Profit in $10,000s');
    py.xlabel('Population of City in 10,000s')
    py.scatter(x,y)
    py.show()

