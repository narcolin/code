import collisions
import data
import vector_math

def closest_collision(intersections, pt):
    smallest_index = 0
    smallest_distance = vector_math.length_vector(vector_math.difference_point(pt, intersections[0][1]))
    for i in range(len(intersections)):
        current_distance = vector_math.length_vector(vector_math.difference_point(pt, intersections[i][1]))
        if smallest_distance > current_distance:
            smallest_index = i
            smallest_distance = current_distance
    return intersections[smallest_index]

def cast_ray(ray, sphere_list, ambientlight, light, eyepoint):
    intersections = collisions.find_intersection_points(sphere_list, ray)
    if len(intersections) == 0:
        white = data.color(1.0, 1.0, 1.0)
        return white
    sphere, point = closest_collision(intersections, ray.pt)
    n = collisions.sphere_normal_at_point(sphere, point)
    pe = vector_math.translate_point(point, vector_math.scale_vector(n, 0.01))
    ldir = vector_math.normalize_vector(vector_math.difference_point(light.point, pe))
    lightcomponent = vector_math.dot_vector(n, ldir)
    if lightcomponent <= 0:
        diffusecontribution = 0
    else:
        diffusecontribution = lightcomponent
        distance = vector_math.length_vector(vector_math.difference_point(pe, light.point))
        intersec = collisions.find_intersection_points(sphere_list, data.ray(pe, ldir))
        for i in range(len(intersec)):
            current_distance = vector_math.length_vector(vector_math.difference_point(intersec[i][1], light.point))
            if current_distance < distance:
                diffusecontribution = 0

    reflectionvector = vector_math.difference_vector(ldir, vector_math.scale_vector(n, (2 * lightcomponent)))
    vdir = vector_math.normalize_vector(vector_math.difference_point(pe, eyepoint))
    specularcontribution = vector_math.dot_vector(reflectionvector, vdir)
    if specularcontribution < 0:
        specularcontribution = 0

    color = sphere.color
    red = (color.r * sphere.finish.ambient * ambientlight.r +
           (diffusecontribution * light.color.r * color.r * sphere.finish.diffuse) +
           light.color.r * sphere.finish.specular * specularcontribution ** (1 / sphere.finish.roughness))
    green = (color.g * sphere.finish.ambient * ambientlight.g +
             (diffusecontribution * light.color.g * color.g * sphere.finish.diffuse) +
             light.color.g * sphere.finish.specular * specularcontribution ** (1 / sphere.finish.roughness))
    blue = (color.b * sphere.finish.ambient * ambientlight.b +
            (diffusecontribution * light.color.b * color.b * sphere.finish.diffuse) +
            light.color.b * sphere.finish.specular * specularcontribution ** (1 / sphere.finish.roughness))

    return data.color(red, green, blue)


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambientlight, light):
    print("P3")
    print(width, height)
    print('255')
    x_step = (max_x - min_x) / width
    y_step = (max_y - min_y) / height
    for j in range(height):
        y = max_y - j * y_step
        for i in range(width):
            x = min_x + i * x_step
            p = data.point(x, y, 0)
            eye_ray = data.ray(eye_point, vector_math.vector_from_to(eye_point, p))
            color = cast_ray(eye_ray, sphere_list, ambientlight, light, eye_point)
            red = min(int(color.r * 255), 255)
            green = min(int(color.g * 255), 255)
            blue = min(int(color.b * 255), 255)
            print(red, green, blue)