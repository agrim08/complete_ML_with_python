'''function copy'''
def welcome():
    print("welcome here")

wel = welcome #just creating copy of welcome
print(wel)
wel()
del welcome
wel()
print(wel)

'''clousers'''
# def main_func():
#     msg = "hello from main func"
#     def sub_func():
#         print("Hello from sub func")
#         print(msg)
#         print("bye bye")

#     # return sub_func
#     return sub_func()

# main_func()

def main_func(func,lst):
    def sub_func():
        print("Hello from sub func")
        # func("hello from print")
        # print(func(lst))
        # print("bye bye")

    # return sub_func
    return sub_func()

# main_func(print)
# main_func(max , [7,99,100102,2,-1,66,36387,8,00,-2])