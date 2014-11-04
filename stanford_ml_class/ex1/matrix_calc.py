__author__ = 'leon'

import numpy as np

x = np.arange(9).reshape((3, 3))
y = np.arange(3)
print x
print y
print np.dot(x, y)

a = np.array([[1, 2], [3, 4]])
print a
print a.T  # matrix transpose

a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
print np.dot(a, b)
print np.dot(a.T, b.T)