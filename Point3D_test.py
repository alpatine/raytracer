from math import sqrt
from unittest import TestCase

from Point3D import Point3D
from Vector3D import Vector3D


class Test_Point3D(TestCase):
    def setUp(self):
        self.a = Point3D(1, 1, 1)
        self.b = Point3D(1.5, -2, 3)
        self.u = Vector3D(2, 2.5, 2)
        self.c = 5
    
    def test_equality(self):
        self.assertEqual(self.a == Point3D(1, 1, 1), True)
        self.assertEqual(self.a == self.b, False)
    
    def test_add(self):
        self.assertEqual(self.a + self.u, Point3D(3, 3.5, 3))
        self.assertEqual(self.b + self.u, Point3D(3.5, 0.5, 5))

    def test_sub(self):
        self.assertEqual(self.a - self.u, Point3D(-1, -1.5, -1))
        self.assertEqual(self.b - self.u, Point3D(-0.5, -4.5, 1))
        self.assertEqual(self.a - self.b, Vector3D(-0.5, 3, -2))
    
    def test_scaler_mul(self):
        self.assertEqual(int(self.c) * self.a, Point3D(5, 5, 5))
        self.assertEqual(float(self.c) * self.a, Point3D(5, 5, 5))
        self.assertEqual(self.a * int(self.c), Point3D(5, 5, 5))
        self.assertEqual(self.a * float(self.c), Point3D(5, 5, 5))
