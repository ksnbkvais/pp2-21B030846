#Write a Python program to calculate the area of regular polygon.
#Area = (number of sides × length of one side × apothem)/2
#Apothem = [(length of one side)/{2 ×(tan(180/number of sides))}].
import math
n=int(input())
l=int(input())
apothem=l/(2*(math.tan(math.pi/n)))
print(int((n*l*apothem)/2))