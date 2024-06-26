# positional arguments:
# def print_val(*args):
#     for val in args:
#         print(val)
        
# print_val(1,2,3,"hi",[0,0,0])

# keyword Arguments: all the parameters i  key-value pair
# def print_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
        
# print_details(name = "Agrim", age = "19", city = "noida")


#combining both:
def print_both(*args, **kwargs):
    for val in args:
        print(val)
        
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        
print_both(1,2,3,name = "Agrim", age = "19", city = "noida")