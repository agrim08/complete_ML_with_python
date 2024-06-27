def outer():
    print("hello outer")
    def inner():
        print("Hello inner")
    
    return inner

fn = outer()
print(fn) #gives innner function
outer()()

def func():
    return lambda msg : print(msg)

func()("Hello")