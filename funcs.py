from math import sqrt

def f(x):
    y = (7*x*x) + (2*x)
    return y

def g(x,y):
    z = (x*x) + (y*y)
    return z

def hypotenuse(x,y):
    h = sqrt(((x-x)**2) + ((y-y)**2))
    return h

def is_positive(x):
    return x > 0