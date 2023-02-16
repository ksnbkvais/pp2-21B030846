import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.xx=x
        self.yy=y
    def show(self):
        print(self.x,self.y)
    def move(self,xx,yy):
        self.x=xx
        self.y=yy
    def distance (self):
        print(math.sqrt((self.x-self.xx)**2+(self.y-self.yy)**2))
ans=Point(int(input()),int(input()))
ans.show()

ans.move(int(input()),int(input()))
ans.show()

ans.distance()






