l = [1, 2, 3]
print(l.count(2))
print(type(l))
print(type(1))

# everything in python is an object

class Sample(object):
    pass
x = Sample()
print(type(x))

class Dog(object):
    species = "mammal" # Class Object Attribute, kind of like a static variable
    # all dog instances will have this

    # __init__ initializes the attributes. It's called automatically when an object is created
    # init is how we define attributes for a class
    # every method of a class has a self argument
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

# sam = Dog() # error: missing 1 required positional argument 'breed'. argument 'self' is provided by default
sam = Dog(breed = 'Huskie', name = 'Sam')

print(sam.breed) # Huskie
print(sam.species) # mammal
print(sam.name) # sam

class Circle(object):
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        # radius ** 2 * pi
        return (self.radius ** 2) * Circle.pi # because pi is a Class Object Attribute

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_radius(self):
        return self.radius

c = Circle(radius = 10)
print(c.area())
print(c.radius)