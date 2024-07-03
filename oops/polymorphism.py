class Animal:
    def eat(self):
        print("Animal eating")

class dog:
    def eat(self):
        print("dog eating")

class cat:
    def eat(self):
        print("cat eating")

a = Animal()
c = cat()
d = dog()

a.eat(), c.eat() , d.eat()

'''2nd way of polymorphism (Duck typing concept)'''
class Birdfly:
    def flyBird(self,bird):
        bird.fly()

class parrot():
    def fly(self):
        print("parrot flying")

class crow():
    def fly(self):
        print("crow flying")

p = parrot()   
c = crow()

bf = Birdfly()
bf.flyBird(p)
bf.flyBird(c)

'''function that demonstrate polymorphism'''
def animal_speek(animal):
    print(animal.speak)
    
