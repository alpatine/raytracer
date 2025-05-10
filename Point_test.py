from math import sqrt
from unittest import TestCase

from Point import Point
from Vector import Vector


class Test_Point(TestCase):
    def setUp(self):
        self.a = Point(1, 1, 1)
        self.b = Point(1.5, -2, 3)
        self.u = Vector(2, 2.5, 2)
        self.c = 5
    
    def test_equality(self):
        self.assertEqual(self.a == Point(1, 1, 1), True)
        self.assertEqual(self.a == self.b, False)
    
    def test_add(self):
        self.assertEqual(self.a + self.u, Point(3, 3.5, 3))
        self.assertEqual(self.b + self.u, Point(3.5, 0.5, 5))

    def test_sub(self):
        self.assertEqual(self.a - self.u, Point(-1, -1.5, -1))
        self.assertEqual(self.b - self.u, Point(-0.5, -4.5, 1))
        self.assertEqual(self.a - self.b, Vector(-0.5, 3, -2))
    
    def test_scaler_mul(self):
        self.assertEqual(int(self.c) * self.a, Point(5, 5, 5))
        self.assertEqual(float(self.c) * self.a, Point(5, 5, 5))
        self.assertEqual(self.a * int(self.c), Point(5, 5, 5))
        self.assertEqual(self.a * float(self.c), Point(5, 5, 5))
