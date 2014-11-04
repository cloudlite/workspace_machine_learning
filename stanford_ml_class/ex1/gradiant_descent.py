__author__ = 'leon'

from numpy import *
import matplotlib.pyplot as plt


def file2matrix(filename):
    fr = open(filename).read()
    lines = fr.splitlines()
    res_matrix = zeros((len(lines), 2))
    i = 0
    for line in lines:
        args = line.split(',')
        res_matrix[i, :] = args[:]
        i += 1

    return res_matrix


def get_theta(data):
    data_size = len(data)
    theta = (0, 0)
    iterations = 1500
    alpha = 0.01
    for i in xrange(iterations):
        tmp0 = theta[0] - alpha * step_size(theta, 0, data)
        tmp1 = theta[1] - alpha * step_size(theta, 1, data)
        theta = (tmp0, tmp1)
    return theta


def step_size(theta, ith, data):
    m = len(data)
    if ith == 0:
        res = 0
        for index in xrange(m):
            res += theta[0] + theta[1] * data[index][0] - data[index][1]
        return res / m
    elif ith == 1:
        res = 0
        for index in xrange(m):
            res += (theta[0] + theta[1] * data[index][0] - data[index][1]) * data[index][0]
        return res / m


def show_plot(data, theta):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 1])

    x = [0, 30]
    y = [theta[0] + theta[1] * x[0], theta[0] + theta[1] * x[1]]
    plt.plot(x, y)
    plt.show()


data = file2matrix("ex1data1.txt")
theta = get_theta(data)
show_plot(data, theta)