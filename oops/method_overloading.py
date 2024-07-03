'''Method Overloading occurs when you define multiple methods with the same name within a class, 
but with different parameter lists'''
class calculator:
    def add(self,a,b): #this func is completely useless
        return a+b
    def add(self,a,b,c):
        return a+b+c

cal = calculator()
print(cal.add(1,2,3))
# print(cal.add(1,2))

#handling method overloading implicitly
from multipledispatch import dispatch
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

product(4, 5)
product(4, 5, 5)

'''Method overloading of magic methods
we have some magic methods like __add__, __sub__ etc.
'''

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other): #this other is some different vector
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self,other): 
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self,other): 
        return Vector(self.x * other.x, self.y * other.y)
    def __eq__(self,other): 
        return (self.x == other.x and self.y == other.y)
    def __repr__(self):
        return f"Vector ({self.x},{self.y})"
    
vec1 = Vector(2,3)
vec2 = Vector(4,5)
print(vec1+vec2)
print(vec1-vec2)
print(vec1*vec2)
print(vec1 == vec2)