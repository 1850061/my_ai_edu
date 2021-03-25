import numpy as np


def target_function(w, b):
    x = 2 * w + 3 * b
    y = 2 * b + 1
    z = x * y
    return x, y, z


def delta_b(x, y, z):
    return z / (3 * y + 2 * x)


def delta_w(x, y, z):
    return z / (x * y)


minn = 1e-5


def change_b(iniW, iniB, targetZ):
    x, y, nowZ = target_function(iniW, iniB)
    bNow = iniB + delta_b(x, y, targetZ - nowZ)
    while np.abs(nowZ - targetZ) > minn:
        print("b={},w={},target={}".format(bNow, iniW, nowZ))
        x, y, nowZ = target_function(iniW, bNow)
        bNow += delta_b(x, y, targetZ - nowZ)
    x, y, z = target_function(iniW, bNow)
    print("b={},w={},target={}".format(bNow, iniW, z))


def change_b_and_w(iniW, iniB, targetZ):
    x, y, nowZ = target_function(iniW, iniB)
    bNow = iniB
    wNow = iniW
    while np.abs(nowZ - targetZ) > minn:
        print("b={},w={},target={}".format(bNow, wNow, nowZ))
        x, y, nowZ = target_function(wNow, bNow)
        bNow += delta_b(x, y, (targetZ - nowZ)/2)
        wNow += delta_w(x, y, (targetZ - nowZ) / 2)
    x, y, z = target_function(wNow, bNow)
    print("b={},w={},target={}".format(bNow, wNow, z))


change_b_and_w(100, 1000, 150)
