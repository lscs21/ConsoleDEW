import numpy

def Gompertz(x, K, A, r,s):
    return (K * numpy.exp(-A * numpy.exp(-r*x)))  

def Richards(x, K, A, r, s):    
    return (K / (( 1 + A * numpy.exp(-r*x))**(1/s)))
