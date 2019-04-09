import numpy
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('data_linear.csv').values

X = numpy.array([data[:, 0]]).T
y = numpy.array([data[:, 1]]).T

plt.scatter(X, y)
plt.xlabel('m2')
plt.ylabel('price')
plt.show()

N = X.shape[0]
one = numpy.ones((N, 1))

XBar = numpy.concatenate((one, X), axis=1)  # 30x2
A = numpy.dot(XBar.T, XBar)  # 2x30 30x2 = 2x2
b = numpy.dot(XBar.T, y)  # 2x30 30x1 = 2x1

w = numpy.dot(numpy.linalg.pinv(A), b)
print(w)

predict = numpy.dot(XBar, w)
plt.plot((XBar[0][1], XBar[N - 1][1]), (predict[0], predict[N - 1]), 'r')
plt.show()

x1 = 50
y1 = w[0] + w[1] * 50
print('50 m2 = ', y1)


