# filter out elements from a list based on a condition:
def even(num):
    if num % 2 == 0:
        return True
l1 = [1,2,3,4,5,6,7,8,9,0]
res = list(filter(even,l1))
print(res)

#filter with lambda
number = [1,2,3,4,5,6,7,8,9,0]
result = list(filter(lambda x: x > 5, number))
print(result)

#filter with multiple conditions:
even_greater_than_5 = list(filter(lambda x : x % 2 ==0 and x > 5,number)) 
print(even_greater_than_5)

#filter on dictionaries:
people = [
    {'name': 'Agrim', 'age': 19},
    {'name': 'Ansh', 'age': 20},
    {'name': 'neha', 'age': 14}
]
    
def age_greater_than_15(person):
    return person['age'] > 15

ans = list(filter(age_greater_than_15,people))
print(ans)