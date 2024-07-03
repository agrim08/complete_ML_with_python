class Animal():
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def eat(self):
        print(self.name + " animal is eating")
    def getype(self):
        print(f"{self.name} is of {self.type} breed")
        

class Dog(Animal):
    def __init__(self, name,type):
        #call the constructor of parent class:
        # Animal.__init__(self,name,type)
        super().__init__(name,type) #calling parent constructor or initializer
        # self.type = type
    def getName(self):
        print(self.name)

#creating object:
dog = Dog("Dhruv","German Shephard")
dog.eat()
dog.getName() 
dog.getype()  


'''**********************SUPER KEYWORD***********************'''
#to accessing parent class property
class Parent:
    property = 90
    def car(self):
        print("parent has a car")
class Child(Parent):
    property = 99
    def car(self):
        print("child has no car") #this is called method overwriting
        
    def display(self):
        print("child property",self.property)
        print("parent property",super().property)
        
    def callCar(self):
        self.car()
        super().car()
        
obj = Child()
obj.display()
obj.callCar()
