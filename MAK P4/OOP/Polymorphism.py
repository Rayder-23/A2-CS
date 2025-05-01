# Polymorphism is a feature of object-oriented programming languages that allows a specific routine
# to use variables of different types at different times.
# Polymorphism in programming gives a program the ability to redefine methods for derived classes.

class Shape:
    def __init__(self,name):
        self.shapename = name
    def area(self): 
        pass # this tells python it is just a dummy variable
    def displayname(self):
        print(self.shapename)

# child is Square, Shape is parent
class Square(Shape):
    def __init__(self,length):
        Shape.__init__(self,"Square")   # defining the values for the parent
        self.length = length            # does not have to be first, order can change
    def area(self):
        return (self.length * self.length)

class Circle(Shape):
    def __init__(self,radius):
        Shape.__init__(self,"Circle")
        self.radius = radius
    def area(self):
        return (self.radius * self.radius * 3.142)

class Rectangle(Shape):
    def __init__(self,length,width):
        Shape.__init__(self,"Rectangle")
        self.length = length
        self.width = width
    def area(self):
        return (self.length * self.width)

# this is why it's useful
shape1 = Circle(3)
shape2 = Square(3)
shape3 = Rectangle(3,4)
print(shape1.area())
print(shape2.area())
print(shape3.area())
shape1.displayname()
shape2.displayname()
shape3.displayname()