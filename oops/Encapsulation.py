'''It involves bundling data (attributes) with the methods (functions) 
that operate on that data within a single unit, typically a class'''
#read more on copilot

class Person():
    def __init__(self,name,car):
        self.__name = name
        self.__car = car

#getters and setters:
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    def getcar(self):
        return self.__car
    def setcar(self,car):
        self.__car = car
        
per = Person("Agrim", "Lamborghini")

print(per.getName())
per.setName("Ansh")
print(per.getName())
