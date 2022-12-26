import vector_math
import math

def sphere_intersection_point(ray, sphere, intersection):
    a = vector_math.dot_Vector(ray.v)
    b = 2 * vector_math.dot_Vector(vector_math.difference_point(ray.pt, sphere.center), ray.vector)
    c = vector_math.dot_Vector(vector_math.difference_point(ray.pt, sphere.center),
                               vector_math.difference_point(ray.pt, sphere.center)) - sphere.rad
    d = math.sqrt((b ** 2) - (4 * a * c))
    t1 = (-1 * b + d) / (2 * a)
    t2 = (-1 * b - d) / (2 * a)

    if d < 0:
        return 'None'
    elif d == 0:
        return t1
    elif t1 > 0 and t2 < 0:
        return t1
    elif t1 < 0 and t2 > 0:
        return t2
    elif t1 < 0 and t2 < 0:
        return 'None'
    elif t1 > 0 and t2 > 0:
        if t1 < t2:
            return t1
        else:
            return t2

def find_intersection_points(sphere_list, ray):
    r = []
    for i in range(len(sphere_list)):
        r.append(sphere_intersection_point(ray, sphere_list[i]))
    return r

def sphere_normal_at_point(sphere, point):
    pov = vector_math.vector_from_to(sphere.center,point)
    return vector_math.normalize_vector(pov)

