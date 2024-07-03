# HAS A test (Aggregation association)
'''ex. man HAS A car'''
'''here both objects can exsist independently'''

#Composition association: 
'''exsistence of 1 obj depends on exsistence of other obj'''
'''ex. Human HAS A heart (heart and human are inter dependent)'''

#aggregation:
class Car():
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

class person():
    def __init__(self,name,car):
        self.name = name
        self.car = car

car = Car("Range Rover", "Black")
per = person("Agrim", car)  #adding car obj to per obj

#composition:
class Engine:
    def engineDetails(self):
        print("car has a v12 engine")

class Tyres:
    def tyresDetails(self):
        print("car has mrf tyres")     

class Doors:
    def doorsDetails(self):
        print("car has automatic doors")

class Car():
    def __init__(self):
        self.engine = Engine()
        self.tyres  = Tyres()     
        self.doors = Doors()
        
    def printDetalils(self):
        self.engine.engineDetails()
        self.tyres.tyresDetails()
        self.doors.doorsDetails()

c = Car()        
c.printDetalils()