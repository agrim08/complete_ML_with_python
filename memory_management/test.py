import sys

a = []
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(b))

del b
print(sys.getrefcount(a))

