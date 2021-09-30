
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


    def contains(self, point: Point):
        if (point.x - self.x)*(point.x - self.x) + (point.y - self.y)*(point.y - self.y) < self.radius*self.radius:
            return True
        else:
            return False


p = Point(2, 5)
c = Circle(0, 0, 10)
if c.contains(p):
    print('SUCCES')