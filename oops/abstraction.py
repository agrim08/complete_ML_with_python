#Abstract class: 
'''https://youtu.be/UDmJGvM-OUw?feature=shared'''
''' 1.can't be initialized (jiska object nhi bana skte)
    2. should have atleast 1 abstarct method

In python we cannot directly create abstarct class, here we use abc inbuilt library(abstract method decorator)
'''

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    # def eat(self):
    #     pass
    def sleep(self):
        pass

# a = Animal()

class Dog(Animal):
    def sleep(self):
        print("Dog is sleeping")
        
d = Dog()
d.sleep()