# Thêm thư viện
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dữ liệu từ excel csv
data = pd.read_csv('data_linear.csv').values
N = data.shape[0]
x = data[:, 0].reshape(-1, 1)
y = data[:, 1].reshape(-1, 1)

# Biểu đồ dữ liệu
plt.scatter(x, y)
plt.xlabel('mét vuông')
plt.ylabel('giá')
plt.show()

# Thêm cột giá trị 1 vào dữ liệu x
x = np.hstack((np.ones((N, 1)), x))

# Khởi tạo giá trị cho w
w = np.array([0., 1.]).reshape(-1, 1)

# Số lần lặp bước 2
numOfIteration = 200

# Mảng để lưu giá trị của hàm số sau mỗi lần lặp
# Để có thể kiểm tra giá trị learning_rate và vẽ đồ thị
cost = np.zeros((numOfIteration, 1))

learning_rate = 0.0000001
for i in range(1, numOfIteration):
    # Tính r = ŷ - y
    r = np.dot(x, w) - y
    # Tính giá trị hàm J
    cost[i] = 0.5 * np.sum(r * r) / N
    # Cập nhật w0 và w1
    w[0] -= learning_rate * np.sum(r)
    w[1] -= learning_rate * np.sum(np.multiply(r, x[:, 1]))
    # In giá trị J sau mỗi lần cập nhật bước 2 để kiểm tra giá trị learning_rate
    print(cost[i])
# Vẽ đường mà máy tính dự đoán sau Gradient descent
predict = np.dot(x, w)
plt.plot((x[0][1], x[N - 1][1]), (predict[0], predict[N - 1]), 'r')
plt.show()
# Sau khi tìm được đường thẳng (w0, w1), việc cuối cùng là dự đoán giá nhà cho nhà 50m^2. 
x1 = 50
y1 = w[0] + w[1] * 50
print('Giá nhà cho 50m^2 là : ', y1) # 755.04
