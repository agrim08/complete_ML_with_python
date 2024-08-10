import numpy as np

arr1 = np.array([1,2,3,4,5])
print(type(arr1))
print(arr1)
print(arr1.shape)

'''1D -> 2D'''
arr2 = np.array([1,2,3,4,5])
arr2.reshape(1,5)
print(arr2)
print(arr2.shape)
# arr2.reshape(1,4) gives error
# print(arr2)

arr3 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr3)
print(arr3.shape)