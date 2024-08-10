my_list = [1,2,3,4]
iterator = iter(my_list)
print(type(iterator))

'''
it uses lazy loading technique,
it does not give me any element until I iterate over it.
'''
#iterating:
print(next(iterator))
'''prints the first element'''
print(next(iterator)) 
'''goes to 2nd element'''
print(next(iterator)) 
'''goes to 3rd element'''
print(next(iterator)) 
'''last eement'''
# print(next(iterator))
'''now if i try, i will get error'''

try:
    print(next(iterator))
except StopIteration:
    print("elements over")

'''iterator on string'''
string = "Agrim"
str_iterator = iter(string)
print(next(str_iterator))