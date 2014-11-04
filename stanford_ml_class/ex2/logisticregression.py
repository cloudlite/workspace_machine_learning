__author__ = 'leon'

from numpy import *
import matplotlib.pyplot as plt


def file2matrix(filename):
    fr = open(filename).read()
    lines = fr.splitlines()
    res_matrix = zeros((len(lines), 3))
    i = 0
    for line in lines:
        args = line.split(',')
        res_matrix[i, :] = args[:]
        i += 1

    labels = res_matrix[:, 2]
    class_label = []
    for label in labels:
        if label == 0.0:
            class_label.append('red')
        elif label == 1.0:
            class_label.append('green')
    return res_matrix, class_label


def show_plot(data, class_label):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 1], c=class_label)
    ax.settitle()
    # x = [0, 30]
    # y = [theta[0] + theta[1] * x[0], theta[0] + theta[1] * x[1]]
    # plt.plot(x, y)
    plt.show()


data_matrix, class_label = file2matrix("ex2data1.txt")
show_plot(data_matrix, class_label)
