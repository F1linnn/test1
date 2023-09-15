import unittest
from Shapes import Circle, Triangle

class MyTestCaseOfShapes(unittest.TestCase):
    def test_circle_area1(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.539, places=2)
    def test_circle_area2(self):
        circle = Circle(10)
        self.assertAlmostEqual(circle.area(), 314.159, places=2)
    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-9)
    def test_zero_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(0)
    def test_negative_triangle_sides(self):
        with self.assertRaises(ValueError):
            triangle =  Triangle(-1,-2,3)
    def test_on_triangle(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(10, 2 ,5)
    def test_triangle_area1(self):
        triangle = Triangle(3,4,5)
        self.assertAlmostEqual(triangle.area(), 6, places=2)
    def test_triangle_area2(self):
        triangle = Triangle(2,4,3)
        self.assertAlmostEqual(triangle.area(), 2.9, places=2)
    def test_triangle_area3(self):
        triangle = Triangle(2,4,4)
        self.assertAlmostEqual(triangle.area(), 3.87, places=2)
    def test_triangle_rectangular1(self):
        triangle = Triangle(3,4,5)
        self.assertTrue(triangle.is_rectangular())
    def test_triangle_rectangular2(self):
        triangle = Triangle(3,7,5)
        self.assertFalse(triangle.is_rectangular())
    def test_triangle_rectangular3(self):
        triangle = Triangle(5,12,13)
        self.assertTrue(triangle.is_rectangular())


if __name__ == '__main__':
    unittest.main()
