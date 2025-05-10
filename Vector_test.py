from math import sqrt
from unittest import TestCase

from Vector import Vector


class Test_Vector(TestCase):
    def setUp(self):
        self.left = Vector(1, 1, 1)
        self.right = Vector(1.5, -2, 3)
        self.a = 5
    
    def test_equality(self):
        self.assertEqual(self.left == Vector(1, 1, 1), True)
        self.assertEqual(self.left == self.right, False)
    
    def test_add(self):
        self.assertEqual(self.left + self.left, Vector(2, 2, 2))
        self.assertEqual(self.left + self.right, Vector(2.5, -1, 4))
        self.assertEqual(self.right + self.right, Vector(3., -4, 6))

    def test_sub(self):
        self.assertEqual(self.left - self.left, Vector(0, 0, 0))
        self.assertEqual(self.left - self.right, Vector(-0.5, 3, -2))
    
    def test_scaler_mul(self):
        self.assertEqual(5 * self.left, Vector(5, 5, 5))
        self.assertEqual(5.0 * self.left, Vector(5, 5, 5))
        self.assertEqual(self.left * 5, Vector(5, 5, 5))
        self.assertEqual(self.left * 5.0, Vector(5, 5, 5))
    
    def test_scalar_div(self):
        self.assertEqual(self.left / 2, Vector(.5, .5, .5))
        self.assertEqual(self.left / 2.0, Vector(.5, .5, .5))
    
    def test_len(self):
        self.assertEqual(self.left.len(), sqrt(3))
        self.assertEqual(self.right.len(), sqrt(15.25))

    def test_len2(self):
        self.assertEqual(self.left.len2(), 3)

    def test_dot(self):
        self.assertEqual(self.left * self.left, 3)
        self.assertEqual(self.left * self.right, 2.5)
        self.assertEqual(Vector(1, 1, 1) * Vector(-1, 1, 0), 0)
    
    def test_cross(self):
        self.assertEqual(self.left ^ self.left, Vector(0, 0, 0))
        self.assertEqual(self.left ^ self.right, Vector(5, -1.5, -3.5))

    def test_negate(self):
        self.assertEqual(-self.left, Vector(-1, -1, -1))
        self.assertEqual(-self.right, Vector(-1.5, 2, -3))
    
    def test_normalise(self):
        x = Vector(2, 2, 2)
        x.normalise()
        self.assertEqual(x, Vector(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)))
    
    def test_hat(self):
        x = Vector(2, 2, 2)
        y = x.hat()
        self.assertEqual(x, Vector(2, 2, 2))
        self.assertEqual(y, Vector(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)))