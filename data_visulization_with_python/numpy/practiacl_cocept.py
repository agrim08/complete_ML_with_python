import numpy as np

data = np.array([1,2,3,4,5])

# mean = data.mean()
mean = np.mean(data)
std_dev = np.std(data)

noramlization = (data - mean)/std_dev
print("Normalized data:",noramlization)

'''logical operations'''
arr = np.array([2,1,3,4,-5,6,8,9,11])
print(arr > 5)
print(arr[arr > 5])
print(arr[(arr > 5) & (arr < 9)])
# print(arr[(arr > 5) and (arr < 9)]) #this will not work