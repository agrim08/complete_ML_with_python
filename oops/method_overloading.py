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