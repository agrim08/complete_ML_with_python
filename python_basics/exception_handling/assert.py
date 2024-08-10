def cube_root(num):
    assert (num >= 0), "Please provide positive number"
    return num**(1/3)

print(cube_root(8))
try:
    val = (cube_root(-8))
    print(val)
except Exception as ex:
    print(ex) #prints the assert line

print("code ends")


