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
    temp = computeCost(x,y,theta)
    for i in range (0,iterations):
        u,v= summ(x,y,theta)
        theta[0]=theta[0]-alpha*u
        theta[1]=theta[1]-alpha*v
    return theta
gradientDescent(x, y, theta=[9,8], alpha=0.01, iterations=1000)
