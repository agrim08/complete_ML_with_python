#map function applies a function to all items on any iterable object and returns map object.

def square(x):
    return x*x

num = [1,2,3,4,5]
print(list(map(square,num)))

print(list(map(lambda y:y*y,num)))

#map multiple iterables:
num1 = [1,2,3]
num2 = [4,5,6]
res = list(map(lambda a,b: a+b,num1,num2))
print(res)

#map to convert list of string to int
str_num = ['1', '2', '3' , '4']
int_num = list(map(int,str_num))
print(int_num)

#map on list of dictionary:
def get_name(person):
    return person['name']

people = [
    {'name': "Agrim", 'age':19},
    {'name': "Ansh", "age": 20}
]
print(list(map(get_name,people)))

