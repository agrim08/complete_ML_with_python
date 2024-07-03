''''        single inheritance      '''
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
        super().__init__(name,type) 
        self.type = type
    def getName(self):
        print(self.name)

''''        multi level inheritance      '''
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
        super().__init__(name,type) 
        self.type = type
    def getName(self):
        print(self.name)

class Pet(Dog):
    def __init__(self,name,type,house):
        super().__init__(name,type)
        self.house = house

'''     hirerichal inheritance      '''
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
        super().__init__(name,type) 
        self.type = type
    def getName(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name,type):
        super().__init__(name,type) 
        self.type = type
    def getName(self):
        print(self.name)

'''     Multiple inheritance      '''
class A:
    def meth1(self):
        print("hello from A")
class B:
    def meth2(self):
        print("hello from B")
        
class C(A,B):
    def meth3(self):
        print("Hello from C")

Cobj = C()
Cobj.meth1()
Cobj.meth2()

#mro: jo phle likha hoga uska method call hoga in case of multiple inheritance
class P:
    def meth1(self):
        print("hello from P")
class Q:
    def meth1(self):
        print("hello from Q")
        
class R(P,Q):
    def meth(self):
        print("Hello from R")

Robj = R()
Robj.meth1()
Robj.meth()
print(R.__mro__)

'''     hybrid inheritance      '''

class Pet(Dog,Cat):
    pass