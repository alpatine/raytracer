from math import sqrt
from typing import Self


class Vector3D:
    def __init__(self: Self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self: Self) -> str:
        return f'Vector3D({self.x},{self.y},{self.z})'
    
    def __eq__(self: Self, other: Self) -> bool:
        if isinstance(other, Vector3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __add__(self: Self, other: Self) -> Self:
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x,
                            self.y + other.y,
                            self.z + other.z)
        else:
            return NotImplemented
        
    def __sub__(self: Self, other: Self) -> Self:
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x,
                            self.y - other.y,
                            self.z - other.z)
        else:
            return NotImplemented
    
    def __mul__(self: Self, other: float | int | Self) -> Self | float:
        if isinstance(other, float) or isinstance(other, int):
            # Scalar product -> Vector3D
            return Vector3D(self.x * other,
                            self.y * other,
                            self.z * other)
        elif isinstance(other, Vector3D):
            # Dot product -> float
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            return NotImplemented
    
    def __rmul__(self: Self, other: float | int | Self) -> Self:
        if isinstance(other, float) or isinstance(other, int):
            return Vector3D(self.x * other,
                            self.y * other,
                            self.z * other)
        else:
            return NotImplemented
    
    def __truediv__(self: Self, other: float | int) -> Self:
        if isinstance(other, float) or isinstance(other, int):
            return Vector3D(self.x / other,
                            self.y / other,
                            self.z / other)
        else:
            return NotImplemented
    
    def len(self: Self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def len2(self: Self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z
    
    def __xor__(self: Self, other: Self) -> Self:
        # Cross product
        if isinstance(other, Vector3D):
            return Vector3D(self.y*other.z - self.z*other.y,
                            self.z*other.x - self.x*other.z,
                            self.x*other.y - self.y*other.x)
        else:
            return NotImplemented

    def __neg__(self: Self) -> Self:
        return Vector3D(-self.x, -self.y, -self.z)

    def normalise(self: Self) -> None:
        length = self.len()
        self.x /= length
        self.y /= length
        self.z /= length
    
    def hat(self: Self) -> Self:
        length = self.len()
        return Vector3D(self.x / length, self.y / length, self.z / length)
