import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", arr)
print("Shape:", arr.shape)  # Output: (2, 3)
print("Number of dimensions:", arr.ndim)  # Output: 2
print("Size (number of elements):", arr.size)  # Output: 6
print("Data type:", arr.dtype)  # Output: int32 (may vary based on platform)
print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on platform)