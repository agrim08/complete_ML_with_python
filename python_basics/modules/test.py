from package.maths import addition
print(addition(3,4))

#or:

from package import maths
print(maths.addition(2,3))

#importing all funcs
from package.maths import *
print(subtraction(9,8))

#importing subpackage
from package.subpackage.divison import divide
print(divide(10,5))

