class Person():
    name = "Agrim"
    age = 19

# obj = Person()  #creating object from Person class
# print(obj)
# print(type(obj))

per = Person()
print(per.name)
print(per.age)

#adding attributes:
per.hobby = "cricket"
per.isLoggedIn = False
print(per.isLoggedIn) #these attributes are specific to per object only

