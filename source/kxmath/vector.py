import math


class Vector2(object):
    def __init__(self, x, y): self.x, self.y = x, y

    # Convertation #
    def __del__(self): del self.x, self.y
    def __str__(self): return f'Vector {__name__} = x: {self.x}, y: {self.y}. Dimensions: 2. Vector2D.'
    def __add__(self, other): return self.x + other.x, self.y + other.y
    def __sub__(self, other): return self.x - other.x, self.y - other.y
    def __float__(self): return float(self.x), float(self.y)
    def __mod__(self, other): return self.x % other.x, self.y % other.y
