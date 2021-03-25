import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def target_function(x, y):
    return x ** 2 + np.sin(y) ** 2


def derivative_function(theta):
    x = theta[0]
    y = theta[1]
    return np.array([2 * x, 2 * np.sin(y) * np.cos(y)])


def show_3d_surface(x, y, z):
    fig = plt.figure()
    ax = Axes3D(fig)

    u = np.linspace(-3, 3, 100)
    v = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(u, v)
    R = np.zeros((len(u), len(v)))
    for i in range(len(u)):
        for j in range(len(v)):
            R[i, j] = X[i, j] ** 2 + np.sin(Y[i, j]) ** 2

    ax.plot_surface(X, Y, R, cmap='rainbow')
    plt.plot(x, y, z, c='black',linewidth = 10)
    plt.show()


if __name__ == '__main__':
    X, Y, Z = [], [], []
    theta = np.array([1, 3])
    error = 1e-3
    step = 0.1
    for i in range(100):
        delta = derivative_function(theta)
        theta = theta - step * delta
        x, y = theta[0], theta[1]
        z = target_function(x, y)
        X.append(x)
        Y.append(y)
        Z.append(z)
        print("x={},y={},z={}".format(x, y, z))
        if delta[0] < error and delta[1] < error:
            break

    show_3d_surface(X, Y, Z)
