import vector_math
import math

def sphere_intersection_point(ray, sphere):
    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = 2 * vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center), ray.dir)
    c = vector_math.dot_vector(vector_math.difference_point(ray.pt, sphere.center),
                               vector_math.difference_point(ray.pt, sphere.center)) - sphere.rad * sphere.rad
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return None
    t1 = (-b + math.sqrt(d)) / (2 * a)
    t2 = (-b - math.sqrt(d)) / (2 * a)

    if t1 < 0:
        if t2 < 0:
            return None
        return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
    elif t2 < 0 or t1 < t2:
        return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
    else:
        return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))





    # if d == 0:
    #     return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
    # elif t1 > 0 and t2 < 0:
    #     return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
    # elif t1 < 0 and t2 > 0:
    #     return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))
    # elif t1 < 0 and t2 < 0:
    #     return None
    # elif t1 > 0 and t2 > 0:
    #     if t1 < t2:
    #         return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t1))
    #     else:
    #         return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.dir, t2))

def find_intersection_points(sphere_list, ray):
    r = []
    for i in range(len(sphere_list)):
        intersection = sphere_intersection_point(ray, sphere_list[i])
        if intersection is not None:
            r.append((sphere_list[i], intersection))
    return r

def sphere_normal_at_point(sphere, point):
    pov = vector_math.vector_from_to(sphere.center, point)
    return vector_math.normalize_vector(pov)

