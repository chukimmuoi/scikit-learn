import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data_linear.csv').values
N = data.shape[0]
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

plt.scatter(x, y)
plt.xlabel('m2')
plt.ylabel('$')
plt.show()

x = np.hstack((np.ones((N, 1)), x))

w = np.array([0., 1.]).reshape(-1, 1)

numOfIteration = 20

cost = np.zeros((numOfIteration, 1))

learning_rate = 0.0000001
for i in range(1, numOfIteration):
    r = np.dot(x, w) - y
    cost[i] = 0.5 * np.sum(r * r) / N
    w[0] -= learning_rate * np.sum(r)
    w[1] -= learning_rate * np.sum(np.multiply(r, x[:, 1]))
    print(cost[i])

predict = np.dot(x, w)
plt.plot((x[0][1], x[N - 1][1]), (predict[0], predict[N - 1]), 'r')
plt.show()

x1 = 50
y1 = w[0] + w[1] * 50
print('50 m2 = ', y1)
