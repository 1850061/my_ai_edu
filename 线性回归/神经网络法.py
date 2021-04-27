import matplotlib.pyplot as plt
import numpy as np
from ReadData import *

filename = "C:\\Users\\ruaner\\Desktop\\ai-edu-master\\ai-edu-master\\A-基础教程\\A2-神经网络基本原理\\Data\\ch04.npz"


class NeuralNet_0_1(object):
    def __init__(self, eta):
        self.eta = eta
        self.w = 0
        self.b = 0

    def __forward(self, x):
        return np.dot(x, self.w) + self.b

    def __backward(self, x, y):
        m = x.shape[0]
        dZ = self.__forward(x) - y
        dW = np.dot(x.T, dZ) / m
        dB = dZ.sum(axis=0, keepdims=True) / m
        return dW, dB

    def __update(self, dw, db):
        self.w = self.w - dw * self.eta
        self.b = self.b - db * self.eta

    def train(self, dataReader):
        X, Y = dataReader.GetWholeTrainSamples()
        dW, dB = self.__backward(X, Y)
        while np.abs(dW) > 1e-4 or np.abs(dB) > 1e-4:
            self.__update(dW, dB)
            dW, dB = self.__backward(X, Y)

    def inference(self, x):
        return self.__forward(x)


def showResult(net, dataReader):
    X, Y = dataReader.GetWholeTrainSamples()
    plt.plot(X, Y, "b.")
    PX = np.linspace(0, 1, 10)
    PZ = net.inference(PX.reshape(10, 1))
    plt.plot(PX, PZ, "r")
    plt.title("Air Conditioner Power")
    plt.xlabel("Number of Servers(K)")
    plt.ylabel("Power of Air Conditioner(KW)")
    plt.show()


if __name__ == '__main__':
    sdr = DataReader_1_0(filename)
    sdr.ReadData()
    eta = 0.1
    net = NeuralNet_0_1(eta)
    net.train(sdr)
    print("w=%f,b=%f" % (net.w, net.b))
    result = net.inference(1.346)
    print("result=", result)
    showResult(net, sdr)
