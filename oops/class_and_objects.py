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
setattr(per,'isLoggedIn', False)
setattr(per,'hobby', 'cricket')
# per.hobby = "cricket"
# per.isLoggedIn = False

print(getattr(per , 'isLoggedIn'))
print(getattr(per , 'hobby'))