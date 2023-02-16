#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.
class Rectangle():
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def area(self):
        return (self.a * self.b)

a=int(input())
b=int(input())

ans=Rectangle(a,b)
print(ans.area())