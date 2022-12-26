import unittest
import cast
import data


class MyTestCase(unittest.TestCase):
    def test_casting(self):
        cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.point(0, 0, -14),
                           [data.sphere(data.point(1, 1, 0), 2, data.color(0, 0, 1), data.finish(.2, .4, .5, .05)), data.sphere(data.point(0.5, 1.5, -3), 0.5, data.color(1, 0, 0), data.finish(.4, .4, .5, .05))],
                           data.color(1, 1, 1), data.light(data.point(-100, 100, -100), data.color(1.5, 1.5, 1.5)))



if __name__ == '__main__':
    unittest.main()
