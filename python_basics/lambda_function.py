# lambda function:
# small,anonymous, 'lambda keyword', can have any number of arguments
# used for short expression or as arguments for higher-order functions

addition = lambda a,b : a+b #declaration
print(addition(5,6))  #calling

even1 = lambda num : num%2 == 0
print(even1(88))

#lambda with map fucntion:
numbers = [1,2,3,4,5,6,7]
print(list(map(lambda x:x**2,numbers)))
