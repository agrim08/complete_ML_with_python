# class Person():
#     name = 'Agrim'
#     age = 19

# per1 = Person()
# per2 = Person()
# per3 = Person()

#initializer:
class Person():
    def __init__(self, name , age):  #self is the obj name and name and age are its attributes
        self.name = name
        self.age = age

per1 = Person("Agrim", 19)
per2 = Person("neha", 27)
per3 = Person("priyanshi", 25)

print(per1.name,'\n',per2.name) 

#classes with optional parameter:
class myself:
    def __init__(self,name ,age = 19, hobby = 'cricket' , student = True):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.student = student

Agrim = myself("Agrim")
print(Agrim.student, Agrim.age)