def main_func(func):

    def sub_func():
        print("Hello from sub func")
        func()
        print("bye bye")
    return sub_func()

def another_func():
    print("learning decorators")

# main_func(another_func)
'''if i want to print all 3 mags without calling main func, we can use decorators'''

@main_func
def another_func():
    print("learning decorators")

''' ****************************************** '''
def my_decorator(func):
    def my_wrapper():
        print("before calling")
        func()
        print("after calling")
    return my_wrapper

@my_decorator
def say_hello():
    print("hello world")

say_hello()

#decorator with arguments:

def repeat(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()