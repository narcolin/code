from math import sqrt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle():
    def __init__(self, p, rad):
        self.center = p
        self.rad = rad

def distance(p1, p2):
    d = sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    return d

def circles_overlap(c1, c2):
    return distance(c1.center, c2.center) < (c1.rad + c2.rad)
