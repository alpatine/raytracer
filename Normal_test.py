from math import sqrt
from unittest import TestCase

from Normal import Normal
from Vector3D import Vector3D


class Test_Normal(TestCase):
    def setUp(self):
        self.n = Normal(1, 1, 1)
        self.m = Normal(1.5, -2, 3)
        self.u = Vector3D(2, 2.5, 2)
        self.a = 5
    
    def test_equality(self):
        self.assertEqual(self.n == Normal(1, 1, 1), True)
        self.assertEqual(self.n == self.m, False)

    def test_negate(self):
        self.assertEqual(-self.n, Normal(-1, -1, -1))
        self.assertEqual(-self.m, Normal(-1.5, 2, -3))
    
    def test_add(self):
        self.assertEqual(self.n + self.n, Normal(2, 2, 2))
        self.assertEqual(self.n + self.m, Normal(2.5, -1, 4))
        self.assertEqual(self.m + self.m, Normal(3., -4, 6))
        self.assertEqual(self.n + self.u, Vector3D(3, 3.5, 3))
        self.assertEqual(self.u + self.n, Vector3D(3, 3.5, 3))
    
    def test_scaler_mul(self):
        self.assertEqual(int(self.a) * self.n, Normal(5, 5, 5))
        self.assertEqual(float(self.a) * self.n, Normal(5, 5, 5))
        self.assertEqual(self.n * int(self.a), Normal(5, 5, 5))
        self.assertEqual(self.n * float(self.a), Normal(5, 5, 5))
    
    def test_dot(self):
        self.assertEqual(self.n * self.u, 6.5)
        self.assertEqual(self.u * self.n, 6.5)
        self.assertEqual(Normal(1, 1, 1) * Vector3D(-1, 1, 0), 0)
        self.assertEqual(Vector3D(1, 1, 1) * Normal(-1, 1, 0), 0)
    
    def test_normalise(self):
        x = Normal(2, 2, 2)
        x.normalise()
        self.assertEqual(x, Normal(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)))
    
    def test_hat(self):
        x = Normal(2, 2, 2)
        y = x.hat()
        self.assertEqual(x, Normal(2, 2, 2))
        self.assertEqual(y, Normal(1/sqrt(3), 1/sqrt(3), 1/sqrt(3)))