import numpy as np
# 1. List to 1-D array and 2 - D array
a = [1, 2, 3, 4]

arr_1d = np.array(a)
arr_2d = np.array([a])

print(arr_1d)
print(arr_2d)

# 2. Array - Shape, Total elements

arr = np.array([[1, 2, 3],[4, 5, 6]])

print("Shape of array:", arr.shape)
print("Total number of elements:", arr.size)

# 3. Array with element lineary spaced 10 elements
x = np.linspace(1, 10, num = 10)
print(x)

# 4. Array with arange with 1 to 10 even number.
arr = np.arange(2, 11, 2)
print(arr)

# 5. Array 2-D to 1-D
a = np.array([[1, 2, 3],[4, 5, 6]])
b = a.flatten()
print(b)

# 6. Add two arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print(np.concatenate((x, y)))

# 7. Show broadcasting.
data = np.array([34, 56])
print(data + 45)

# 8. 1D to 2D array
a = np.array([1, 2, 3, 4, 5, 6, 7])
b = a[np.newaxis, :]
print(b)