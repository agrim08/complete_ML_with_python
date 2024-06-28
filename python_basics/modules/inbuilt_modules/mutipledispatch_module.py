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