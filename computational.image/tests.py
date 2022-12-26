import unittest

import cast
import collisions
import data

class MyTestCase(unittest.TestCase):
    def test_point(self):
        p1 = data.point(1, 2, 3)
        self.assertAlmostEqual(p1.x, 1)
        self.assertAlmostEqual(p1.y, 2)
        self.assertAlmostEqual(p1.z, 3)
        pass

    def test_vector(self):
        p2 = data.vector(1, 2, 3)
        self.assertAlmostEqual(p2.x, 1)
        self.assertAlmostEqual(p2.y, 2)
        self.assertAlmostEqual(p2.z, 3)
        pass

    def test_ray(self):
        a = data.ray(1, 2)
        self.assertAlmostEqual(a.pt, 1)
        self.assertAlmostEqual(a.dir, 2)
        pass

    def test_sphere(self):
        b = data.point(1, 2, 3)
        white = data.color(255, 255, 255)
        c = data.sphere(b, 5, white, data.finish(1, 0, 0, 1))
        self.assertAlmostEqual(c.center.x, 1)
        self.assertAlmostEqual(c.center.y, 2)
        self.assertAlmostEqual(c.center.z, 3)
        self.assertAlmostEqual(c.rad, 5)
        self.assertAlmostEqual(c.color, white)
        pass

    def test_sphere_intersection_point(self):
        ray = data.ray(data.point(3, 0, 0), data.vector(-3, 0, 0))
        sphere = data.sphere(data.point(0, 0, 0), 1, data.color(1, 1, 1), data.finish(1, 0, 0, 1))
        intersection = collisions.sphere_intersection_point(ray, sphere)
        self.assertTrue(intersection == data.point(1, 0, 0))

    def test_find_intersection_points(self):
        ray = data.ray(data.point(4,0,0), data.vector(-5,0,0))
        sphere1 = data.sphere(data.point(0, 0, 0), 1, data.color(1, 1, 1), data.finish(1, 0, 0, 1))
        sphere2 = data.sphere(data.point(-1, 0, 0), 1, data.color(1, 1, 1), data.finish(1, 0, 0, 1))
        sphere3 = data.sphere(data.point(1, 0, 0), 1, data.color(1, 1, 1), data.finish(1, 0, 0, 1))
        sphere_list = [sphere1, sphere2, sphere3]
        intersection = collisions.find_intersection_points(sphere_list, ray)
        self.assertTrue(intersection[0] == (sphere1,data.point(1, 0, 0)))
        self.assertTrue(intersection[1] == (sphere2,data.point(0, 0, 0)))
        self.assertTrue(intersection[2] == (sphere3,data.point(2, 0, 0)))

    def test_sphere_normal_at_point(self):
        point = data.point(0, 0, 0)
        sphere = data.sphere(data.point(1, 0, 0), 1, data.color(1, 1, 1), data.finish(1, 0, 0, 0))
        snap = collisions.sphere_normal_at_point(sphere, point)
        self.assertTrue(snap == data.vector(-1, 0, 0))

    def test_cast_ray(self):
        ray = data.ray(data.point(4, 0, 0), data.vector(-5, 0, 0))
        sphere1 = data.sphere(data.point(0, 0, 0), 1, data.color(0, 0, 0), data.finish(0, 0, 0, 1))
        sphere2 = data.sphere(data.point(-1, 0, 0), 1, data.color(1, 1, 1), data.finish(1, 0, 0, 1))
        sphere3 = data.sphere(data.point(1, 0, 0), 1, data.color(.5, .5, .5), data.finish(.5, 0, 0, 1))
        sphere_list = [sphere1, sphere2, sphere3]
        light = data.light(data.point(0, 0, 0), data.color(0, 0, 0))
        color = cast.cast_ray(ray, sphere_list, data.color(0, .5, 1), light, data.point(0, 0, 0))

        self.assertEqual(color, data.color(0, .125, .25))

if __name__ == '__main__':
    unittest.main()

