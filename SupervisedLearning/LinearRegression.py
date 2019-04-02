"""
================================================== =======
Ví dụ hồi quy tuyến tính
================================================== =======
Ví dụ này sử dụng tính năng duy nhất đầu tiên của bộ dữ liệu `bệnh tiểu đường, trong
để minh họa một âm mưu hai chiều của kỹ thuật hồi quy này. Các
đường thẳng có thể được nhìn thấy trong cốt truyện, cho thấy cách hồi quy tuyến tính cố gắng
để vẽ một đường thẳng sẽ tối thiểu hóa tổng bình phương còn lại
giữa các phản hồi quan sát được trong tập dữ liệu và các phản hồi được dự đoán bởi
các xấp xỉ tuyến tính.

Các hệ số, tổng bình phương còn lại và điểm phương sai cũng
tính toán.

"""
print(__doc__)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Tai tap du lieu benh tieu duong.
benhTieuDuong = datasets.load_diabetes()

# Chi su dung mot tinh nang.
benhTieuDuong_X = benhTieuDuong.data[:, np.newaxis, 2]

# Tách dữ liệu vào đào tạo / thử nghiệm bộ.
benhTieuDuong_X_train = benhTieuDuong_X[:-20]
benhTieuDuong_X_test = benhTieuDuong_X[-20:]

# Tách các mục tiêu vào đào tạo / thử nghiệm bộ.
benhTieuDuong_y_train = benhTieuDuong.target[:-20]  # 0 -> size - 20
benhTieuDuong_y_test = benhTieuDuong.target[-20:]  # size - 20 -> size

# Tạo đối tượng hồi quy tuyến tính.
linearRegression = linear_model.LinearRegression()

# Huấn luyện mô hình bằng cách sử dụng tập huấn luyện
linearRegression.fit(benhTieuDuong_X_train, benhTieuDuong_y_train)

# Hãy dự đoán sử dụng các thiết lập thử nghiệm.
benhTieuDuong_y_dudoan = linearRegression.predict(benhTieuDuong_X_test)

# Các hệ số
print('Coefficients (Hệ số): ', linearRegression.coef_)
# Giá trị trung bình bình phương lỗi
print('Mean squared error (Có nghĩa là lỗi bình phương): %.2f' % mean_squared_error(benhTieuDuong_y_test, benhTieuDuong_y_dudoan))
# Giải thích điểm sai: 1 là dự đoán hoàn hảo
print('Variance score (Điểm phương sai): %.2f' % r2_score(benhTieuDuong_y_test, benhTieuDuong_y_dudoan))

# Lô đầu ra
plt.scatter(benhTieuDuong_X_test, benhTieuDuong_y_test, color='black')
plt.plot(benhTieuDuong_X_test, benhTieuDuong_y_dudoan, color='blue', linewidth=3)

plt.xticks()
plt.yticks()

plt.show()

