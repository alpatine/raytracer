from math import sqrt
from typing import Self

from Vector3D import Vector3D


class Point3D:
    def __init__(self: Self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self: Self) -> str:
        return f'Point3D({self.x},{self.y},{self.z})'
    
    def __eq__(self: Self, other: Self) -> bool:
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __add__(self: Self, other: Self) -> Self:
        if isinstance(other, Vector3D):
            return Point3D(self.x + other.x,
                            self.y + other.y,
                            self.z + other.z)
        else:
            return NotImplemented
        
    def __sub__(self: Self, other: Self) -> Self:
        if isinstance(other, Point3D):
            return Vector3D(self.x - other.x,
                            self.y - other.y,
                            self.z - other.z)
        elif isinstance(other, Vector3D):
            return Point3D(self.x - other.x,
                            self.y - other.y,
                            self.z - other.z)
        else:
            return NotImplemented
    
    def __mul__(self: Self, other: float | int | Self) -> Self | float:
        if isinstance(other, float) or isinstance(other, int):
            # Scalar product -> Point3D
            return Point3D(self.x * other,
                            self.y * other,
                            self.z * other)
        else:
            return NotImplemented
    
    def __rmul__(self: Self, other: float | int | Self) -> Self:
        if isinstance(other, float) or isinstance(other, int):
            return Point3D(self.x * other,
                            self.y * other,
                            self.z * other)
        else:
            return NotImplemented
