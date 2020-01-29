def feedforward_cost(x,y,examples,lamda):
    m=examples
    x=np.hstack((np.ones((m,1)),x))
    z1=np.dot(x,theta1.T)
    a1=sigmoid(z1)
    a1=np.hstack((np.ones((m,1)),a1))
    z2=np.dot(a1,theta2.T)
    a2=sigmoid(z2)
    print(a2.shape)
    y_i=np.zeros((m,10))
    for i in range(0,m): #converting y(1,300) array to 5000,10 sized array
        element=y[i]
        y_i[i,element-1]=1  
    cost = (1/m) * np.sum ( np.sum ((-y_i.T) * np.log(h_theta) - (1-y_i.T) * np.log(1-h_theta) ))
    t1=theta1[:,1:]
    t2=theta2[:,1:]
    regularised=(lamda/(2*m))*np.sum(np.sum(np.square(t1))+np.sum(np.square(t2)))
    return regularised+cost
def backpropogation(x,m,y,lambd):
    a=[x]
    z=[]
    Theta_grad=[]
    Theta1_grad=0
    x=np.hstack((np.ones((m,1)),x))
    z1=np.dot(x,theta1.T)
    z.append(z1)
    a1=sigmoid(z1)
    a.append(a1)
    a1=np.hstack((np.ones((m,1)),a1))
    z2=np.dot(a1,theta2.T)
    z.append(z2)
    a2=sigmoid(z2)
    a.append(a2)
    y_i=np.zeros((m,10))
    for i in range(0,m): #converting y array to 5000,10 sized array
        element=y[i]
        y_i[i,element-1]=1  
    delta_3=(a[-1]-y_i)
    z[-2]=np.hstack((np.ones((m,1)),z[-2]))
    thet2=theta2[:,1:]
    delta_2=(np.dot(theta2.T,delta_3.T).T*sigmoid_grad(z[-2]))
    print(delta_2.shape)
    print(a[0].shape)
    Theta2_grad = ((1/m)+(np.dot(delta_3.T,a[1]))) # '; % (10*1)*(1*26)
    Theta1_grad = ((1/m)+(np.dot(delta_2.T,a[0])))
    Theta2_grad=((1/m)+(np.dot(delta_3.T,a[1])))+((lambd/m)*theta2[:,1:])
    Theta_grad.append(Theta1_grad)
    Theta_grad.append(Theta2_grad)
    return Theta_grad

