from math import sqrt
from typing import Self

from Vector import Vector


class Normal:
    def __init__(self: Self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self: Self) -> str:
        return f'Normal3D({self.x},{self.y},{self.z})'
    
    def __eq__(self: Self, other: Self) -> bool:
        if isinstance(other, Normal):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __neg__(self: Self) -> Self:
        return Normal(-self.x, -self.y, -self.z)

    def __add__(self: Self, other: Self) -> Self:
        if isinstance(other, Normal):
            return Normal(self.x + other.x,
                            self.y + other.y,
                            self.z + other.z)
        elif isinstance(other, Vector):
            return Vector(self.x + other.x,
                            self.y + other.y,
                            self.z + other.z)
        else:
            return NotImplemented
    
    def __radd__(self: Self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return NotImplemented
    
    def __mul__(self: Self, other: float | int | Self) -> Self | float:
        if isinstance(other, float) or isinstance(other, int):
            # Scalar product -> Normal3D
            return Normal(self.x * other,
                            self.y * other,
                            self.z * other)
        elif isinstance(other, Vector):
            # Dot product -> float
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return NotImplemented
    
    def __rmul__(self: Self, other: float | int | Self) -> Self | int | float:
        if isinstance(other, float) or isinstance(other, int):
            return Normal(self.x * other,
                            self.y * other,
                            self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return NotImplemented
    
    def normalise(self: Self) -> None:
        length = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x /= length
        self.y /= length
        self.z /= length
    
    def hat(self: Self) -> Self:
        length = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        return Normal(self.x / length, self.y / length, self.z / length)
