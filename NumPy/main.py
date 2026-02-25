import numpy as np

print(np.__version__)
a = np.array([23, 34, 56 ,10, 78, 50])
print(a.sum())
print(a)
print(type(a))

# b = np.array([[1, 2, 3], [4, 5 ,6], [7, 8, 9]])
# print(b)
# print(type(b))
# print(b[2,2])

# print(a.ndim) # To check th dimentions
# print(a.shape) # To check the row and columns
# print(a.size) # TO get the size of the array
# print(a.dtype)# To check the datatype

# print(np.zeros((3, 5)))
# print(np.ones((3, 5), dtype=int))
# print(np.empty(10))
# print(np.arange(2, 21, 2))
# print(np.arange(20, 1, -2))
# print(np.arange(5, 51, 5))
# print(np.arange(50, 4, -5)) 
# print(np.eye(7))

# a = np.array([23, 34, 56 ,10, 78, 50])
# b = np.array([34, 45, 45, 12, 57, 96])

# print(np.concatenate((a, b)))

# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6]])

# print(np.concatenate((x, y), axis = 0))

# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])

# print(np.concatenate((x, y), axis = 1))

# array = np.array([[[0, 1, 2, 3,], [4, 5, 6, 7]],[[0, 1, 2, 3,], [4, 5, 6, 7]],[[0, 1, 2, 3,], [4, 5, 6, 7]]])
# print(array)
# print(array.ndim) # To check th dimentions
# print(array.shape) # To check the row and columns
# print(array.size) # TO get the size of the array


# a1 = np.array([[1, 1], [2, 2]])
# a2 = np.array([[3, 3], [4, 4]])

# print(np.vstack((a1, a2)))
# print(np.hstack((a1, a2)))

# print(np.arange(1, 36).reshape(5, 7))

# x = np.arange(1, 36).reshape(5, 7)
# print(np.hsplit(x, 3))

# a = np.array([1, 2, 3, 4, 5])
# c = a[np.newaxis, :]
# c = np.expand_dims(a, axis = 0)
# print(c)
# print(c.shape)
# print(c.ndim)
# c = a[:, np.newaxis]
# c = np.expand_dims(a, axis = 1)
# print(c)
# print(c.shape)
# print(c.ndim)

# data = np.array([1, 2, 3])
# print(data[1])
# print(data[0:2])
# print(data[1:])
# print(data[-1:])

# x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(x[x%2!=0])

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(np.nonzero(a<=7))

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# b = a[0, :]
# print(b)
# b[0] = 99
# print(b)
# print(a)

# c = a.copy()
# c[0] = 96
# print(c)
# print(a)

# Broadcasting
# data = np.array([34, 56])
# print(data + 45)

# rng = np.random.default_rng()
# print(rng.random((2, 8)))
# print(rng.integers(6))
# print(rng.integers(7, size=(4, 8)))

# a = np.array([11, 11, 12, 12, 13, 14, 14, 16, 15, 16])
# print(np.unique(a))
# print(np.unique(a, return_index = True))
# print(np.unique(a, return_counts = True))
