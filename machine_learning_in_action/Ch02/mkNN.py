__author__ = 'leon'

from numpy import *
import matplotlib.pyplot as plt


def file2matrix(filename):
    file = open(filename, 'r')
    lines = file.read().splitlines()
    numOfLines = len(lines)
    res = zeros((numOfLines, 3))
    classLabelVector = []

    colorDict = {'1': 'red', '2': 'blue', '3': 'green'}
    i = 0
    for line in lines:
        args = line.split()
        res[i, :] = args[0:3]
        classLabelVector.append(colorDict[args[-1]])
        i += 1

    return res, classLabelVector


data, label = file2matrix("datingTestSet2.txt")
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:, 1], data[:, 2], c=label)
plt.show()