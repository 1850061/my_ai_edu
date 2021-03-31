import numpy as np
import matplotlib.pyplot as plt


def cal_w(X, Y, m):
    p = m * sum(X * Y) - sum(X) * sum(Y)
    q = m * sum(X ** 2) - (sum(X)) ** 2
    return p / q


def cal_b(X, Y, m, w):
    return (sum(Y - w * X)) / m


def target_function(x, w, b):
    return w * x + b


X = np.array([1, 3, 6, 9, 15])
Y = np.array([2, 5, 9, 10, 19])
w = cal_w(X, Y, X.shape[0])
b = cal_b(X, Y, X.shape[0], w)
x = np.linspace(0, 20, 100)
plt.plot(x, target_function(x, w, b))
plt.plot(X, Y, 'o')
plt.show()
print("w:{},b:{}".format(w, b))
