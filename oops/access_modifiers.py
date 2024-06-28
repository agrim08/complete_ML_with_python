'''In Python, access modifiers control the visibility of class 
attributes and methods from outside the class.
there are three types:
1.public:- accessible from anywhere in the program. (default)
2.protected:- Members declared as protected are accessible within the class and its subclasses.
3.private :- accessible only within the class.
'''

#public:
class person:
    def __init__(self,name):
        self.name = name

per = person("Agrim")
print(per.name)

#protected:
class Student:
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    def _displayRollAndBranch(self):
        print("Roll:", self._roll)
        print("Branch:", self._branch)

class Geek(Student):
    def displayDetails(self):
        print("Name:", self._name)
        self._displayRollAndBranch()

obj = Geek("R2J", 1706256, "IT")
obj.displayDetails()  
# Output: Name: R2J, Roll: 1706256, Branch: IT

#private:
class myself:
    def __init__(self,name,salary ,age = 19, hobby = 'cricket' , student = True):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.student = student
        self.__salary = salary #this is private
    
    def accessSalary(self):
        print(self.__salary)
        self.__privateFunc()
    
    def __privateFunc(self):
        print("done")

Agrim = myself("Agrim",50000)
print(Agrim.student, Agrim.age)
# Agrim.accessSalary() #this will call privateFunc
# print(Agrim.__salary) #does not work
# Agrim.__privateFunc() #does not work

'''***************Reading Private Attributes*********************'''

print(Agrim._myself__salary)
print(Agrim._myself__privateFunc())