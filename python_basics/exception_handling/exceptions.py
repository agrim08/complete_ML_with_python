#exception handling allows you to handle errors gracefully and take corrective actions without stopping the execution of the program.
# https://www.w3schools.com/python/python_ref_exceptions.asp

a = 10
# a = b name error

#handling: try except block

# 1. Name Error
try:
    a = b
except:
    print("the variable has not been assigned")
#or:
try:
    a = c
except NameError as ex:
    print(ex)

# 2. Zero divison error
try:
    result = 10/0
except ZeroDivisionError as ex:
    print(ex)

# 3. more errors:
a = 10
# try:
#     result = 10/2
#     a = c
# except ZeroDivisionError as ex:
#     print(ex)

# 4. to solve above problem:
a = 10
try:
    result = 10/2
    a = c
except ZeroDivisionError as ex:
    print(ex)
except Exception as ex1: #this exception is the parent class of all errors
    print(ex1)

# 5. value error:
try: 
    num = int(input("Enter a num"))
    res = 10/num
except ValueError:
    print("enter a valid num")
except ZeroDivisionError:
    print("cannot divide by zero")

# try except else:
try: 
    num = int(input("Enter a num"))
    res = 10/num
except ValueError:
    print("enter a valid num")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(f"the result is {res}") #this block will be executed if no error occured
    
#finally block:
try: 
    num = int(input("Enter a num"))
    res = 10/num
except ValueError:
    print("enter a valid num")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(f"the result is {res}")
finally:
    print("this will execute everytime no matter error occured or not")