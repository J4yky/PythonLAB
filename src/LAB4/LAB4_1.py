"""
Utwórz nowy skrypt i zdefiniuj w nim klasę Punkt, która będzie definiowała obiekt
(punkt) w przestrzeni dwuwymiarowej (domyślnie na początku układu współrzędnych (0,0))
oraz będzie posiadała dwie metody: odleglosc – zwracającą odległość punktu od
początku układu współrzędnych oraz dystans – zwracająca odległość między dwoma
punktami (obiektami należącymi do klasy Punkt). Ponadto zdefiniuj w klasie Punkt
dwie metody specjalne __repr__ oraz __str__ , które pozwolą na wyświetlenie
współrzędnych punktu. Uzupełnij skrypt (stwórz kilka punktów – tj. obiektów klasy Punkt) i przetestuj jego
działanie.
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
        return f"Point with coordinates: ({self.x}, {self.y})"

point0 = Point()
point1 = Point(3, 4)
point2 = Point(5, 6)

print(point0)
print(point1)
print(point2)

print("Point1 distance from the start: ", point1.distance_from_the_start())
print("Point2 distance from the start: ", point2.distance_from_the_start())

print("Point1 distance from point0:", point1.distance_from_another_point(point0))
print("Point2 distance from point0:", point2.distance_from_another_point(point0))
print("Point2 distance from point1:", point2.distance_from_another_point(point1))