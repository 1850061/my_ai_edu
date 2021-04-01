import numpy as np
import matplotlib.pyplot as plt


def loss(X, Y, b, w, m):
    return sum((Y - w * X - b) ** 2) / (2 * m)


def target_function(x, w, b):
    return w * x + b


def change_w_b(X, Y, w, b, m):
    Z = X * w + b
    dw = sum((Z - Y) * X) / m
    db = sum(Z - Y) / m
    return dw, db


X = np.array([1, 3, 6, 9, 15])
Y = np.array([2, 5, 9, 10, 19])
step = 0.01
w, b = 0, 0
error = 1e-5

for i in range(100):
    dw, db = change_w_b(X, Y, w, b, X.shape[0])
    if abs(dw) < error and abs(db) < error:
        break
    w = w - step * dw
    b = b - step * db

x = np.linspace(0, 20, 100)
plt.plot(x, target_function(x, w, b))
plt.plot(X, Y, 'o')
plt.show()
print("w:{},b:{}".format(w, b))
