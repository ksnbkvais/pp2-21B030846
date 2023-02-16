#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape():
    def __init__(self, a=0):
        self.a = a

    def area(self):
        print(self.a * self.a)

class Square(Shape):
    def __init__(self, a):
        self.a=a
    def area(self):
        print(self.a * self.a)
   
s=Shape()
s.area()

l=Square(int(input()))
l.area()