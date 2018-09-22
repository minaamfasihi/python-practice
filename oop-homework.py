class Line(object):
    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        return ((((self.coord2[1] - self.coord1[1]) ** 2) + ((self.coord2[0] - self.coord1[0]) ** 2)) ** 0.5)

    def slope(self):
        return (self.coord2[1] - self.coord1[1]) / (self.coord2[0] - self.coord1[0])

coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance()) # 9.4333
print(li.slope()) # 1.6


class Cylinder(object):
    PI = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (Cylinder.PI * ((self.radius) ** 2) * self.height)

    def surface_area(self):
        return 2 * ((Cylinder.PI * self.radius * self.height) + (Cylinder.PI * (self.radius ** 2)))

c = Cylinder(2, 3)
print(c.volume()) # 113.039
print(c.surface_area()) # 91.68