#Create a generator that generates the squares of numbers up to some number N.
def privet(n):
    for i in range (n):
        yield i**2
a= int(input())
for x in privet(a):
    print(x)
