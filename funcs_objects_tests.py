import unittest
import objects

class TestCases(unittest.TestCase):
   def test_cases(self):
      p1 = objects.Point(1, 2)
      self.assertEqual(p1.x, 1)
      self.assertEqual(p1.y, 2)
      pass

   def test_circle(self):
      p1 = objects.Point(1, 2)
      c1 = objects.Circle(2, 7)
      self.assertEqual(c1.center, 2)
      self.assertEqual(c1.rad, 7)
      pass

   def test_distance(self):
      p1 = objects.Point(3, 7)
      p2 = objects.Point(5, 8)
      self.assertEqual(p1.x, 3)
      self.assertEqual(p2.x, 5)
      self.assertEqual(p1.y, 7)
      self.assertEqual(p2.y, 8)
      pass

   def test_circles_overlap(self):
      c1 = objects.Circle(objects.Point(4, 5),3)
      c2 = objects.Circle(objects.Point(4, 1), 7)
      self.assertEqual(c1.center.x, 4)
      self.assertEqual(c1.rad, 3)
      self.assertEqual(c2.center.y, 1)
      self.assertEqual(c1.rad, 3)
      self.assertTrue(objects.circles_overlap(c1, c2))
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()