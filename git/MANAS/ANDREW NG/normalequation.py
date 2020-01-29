def normal(b,y):
    temp1=b.transpose().dot(b)
    theta=(np.linalg.inv(temp1).dot(b.transpose())).dot(y)
    print(theta)
    return theta
normalisation(x,y)


