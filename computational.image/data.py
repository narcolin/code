import utility

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        return utility.epsilon_equal(self.x == other.x, self.y == other.y, self.z == other.z)

class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, other):
        return utility.epsilon_equal(self.x == other.x, self.y == other.y, self.z == other.z)

class ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir
    def __eq__(self, other):
        return utility.epsilon_equal(self.pt == other.pt, self.ray == other.ray)

class sphere:
    def __init__(self, center, rad, color, finish):
        self.center = center
        self.rad = rad
        self.color = color
        self.finish = finish
    def __eq__(self, other):
        return utility.epsilon_equal(self.center == other.center, self.rad == other.rad, self.color == other.color, self.finish == other.finish)

class color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __eq__(self, other):
        return utility.epsilon_equal(self.r == other.r, self.g == other.g, self.b == other.b)

class finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness
    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient == other.ambient, self.diffuse == other.diffuse, self.specular == other.specular, self.roughness == other.roughness)

class light:
    def __init__(self, point, color):
        self.point = point
        self.color = color
    def __eq__(self, other):
        return utility.epsilon_equal(self.point == other.point, self.color == other.color)

