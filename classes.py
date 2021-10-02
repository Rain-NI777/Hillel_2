
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius


    def contains(self, point: Point):
        if (point.x - self.x)**2 + (point.y - self.y)**2 < self.radius**2:
            return True
        else:
            return False


class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def square(self):
        return (self.base * self.height) / 2


class Parallelogram(Shape):
    def __init__(self, x, y, side, height):
        super().__init__(x, y)
        self.side = side
        self.height = height

    def square(self):
        return (self.side * self.height)


p = Point(3, 2)
c = Circle(2, 1, 4)
t = Triangle(2, 6, 5, 7)
par = Parallelogram(1, 2, 7, 9)
print(p.x, p.y)
print(c.x, c.y, c.radius)
print(t.square())
print(par.square())