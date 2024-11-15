"""
Uzupełnij klasę Kolo o metodę przesun, która będzie przesuwała kolo na płaszczyźnie o
podany wektor (argument metody to krotka (x,y) lub lista [x,y] ze współrzędnymi wektora).
"""
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_from_the_start(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_from_another_point(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"Point with coordinates: ({self.x}, {self.y})\n"

class Circle(Point):
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x,y)
        self.r = r

    def area(self):
        return math.pi*self.r**2

    def circumference(self):
        return 2*math.pi*self.r

    def move(self, other):
        self.x += other[0]
        self.y += other[1]

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.r})"

    def __str__(self):
        return f"Circle with center in ({self.x}, {self.y}) and radius ({self.r})"



point0 = Point()
point1 = Point(2, 6)
point2 = Point(-1, 8)

move_by = [1,5]

print(point0)
print(point1)
print(point2)

circle0 = Circle()
circle1 = Circle(point1.x, point1.y, 3)
circle2 = Circle(point2.x, point2.y, 6)

print(circle0)
print("Circle area: ", circle0.area())
print("Circle circumference: ", circle0.circumference())
print("")

print(circle1)
print("Circle area: ", circle1.area())
print("Circle circumference: ", circle1.circumference())
print("")

print(circle2)
print("Circle area: ", circle2.area())
print("Circle circumference: ", circle2.circumference())
print("")

circle0.move(move_by)
print(circle0)
print("Circle area: ", circle0.area())
print("Circle circumference: ", circle0.circumference())
print("Circle distance from the start: ", circle0.distance_from_the_start())