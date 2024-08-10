''' simpler way to create iterators, uses "yield" keyword '''

def square(n):
    for i in range(n):
        # return i**2
        yield i**2

# print(square(3)) check o/p differnece, if we use return
for i in square(5):
    print(i)

a = square(4)
for i in range(5):
    try:
        print(next(a))
    except StopIteration:
        print("elements over")

#example 2:
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
for num in gen:
    print(num)

#practical example : reading large files
'''generator allow to process one line at a time without loading entire file in memory'''
def file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

file_path='large_file.txt'
for line in file_reader(file_path):
    print(line.strip())