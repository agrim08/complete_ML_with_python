#double underscore methods:
'''
1. __init__ new instance of class
2. __str__ return string representation of object
3. __repr__ return official string representation of object
4. __len__ return len of obj
5. __getitem__
6. __setitem__
'''

'''
class Person:
    pass

per = Person()
print(dir(per))
'''

#basic magic methods:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    #overwriting method
    def __str__(self):
        return f"{self.name},{self.age} years old"
    
    def __repr__(self) -> str:
        return f"Person (name is {self.name} and age is {self.age})"
        
per = Person("Agrim",19)
print(per)
print(repr(per))