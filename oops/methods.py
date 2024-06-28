#instance method
class Person():
    country = "India"
    
    @classmethod #this is decorator
    def greet(msg):
        print(f"Hello from {msg.country}") #this function will have access to class properties
        
    @staticmethod
    def hello():
        print(f"hello from {country}") #this static method has no access to class properties
    
    def __init__(self, name , age):  
        self.name = name
        self.age = age
        
    def findAge(self):  #this is called instance method
        return self.age
per = Person("Agrim",19)
print(per.findAge())

Person.greet()
per.greet()
per.hello()

#notes:
#class method can be called by class and object
#it has no access to object properties but has access to class properties