# installing numpy
# pip install numpy

# importing the numpy library
import numpy as np

a = [1,2,3,4,5,6,7,8,9,10,11,12]

# converting a array into a numpy array
a_array = np.array(a)
print(a_array)
print(type(a_array))

# creating a new array with zeros
n = 10
a1 = np.zeros(n)
print(a1)
b1  =np.zeros(n, int)
print(b1)

# creating an array of n elements with uniformly distributed values in an intervale [p,q]
n = np.linspace(0,1,10)
print(n)

# creating an array of specified range
# arange(start, stop, step)
specified_range = np.arange(10, 20, 3)
print(specified_range)

new_array =  np.array([[1,2,3], [4,5,6]])
print(new_array)
# converting to 1D array
print(new_array.flatten())

# generating sequence of random numbers
# np.random.normal(mean, sd, size)

matrix_1 = np.array([[1,2], [3,4]])
matrix_2 = np.array([[4,5], [6,7]])

# element wise matrix multiplication
print(np.multiply(matrix_1, matrix_2))

# dot product
print(np.matmul(matrix_1, matrix_2))

# shape
print(matrix_1.shape)














