"""
================================================== =========
Plot Ridge hệ số như là một chức năng của chính quy
================================================== =========

Cho thấy ảnh hưởng của cộng tuyến trong các hệ số của công cụ ước tính.

.. currentmodule :: sklearn.linear_model

: class: `Ridge` Regression là công cụ ước tính được sử dụng trong ví dụ này.
Mỗi màu đại diện cho một tính năng khác nhau của
vectơ hệ số, và điều này được hiển thị như là một hàm của
tham số chính quy.

Ví dụ này cũng cho thấy sự hữu ích của việc áp dụng hồi quy Ridge
để ma trận điều hòa cao. Đối với ma trận như vậy, một chút
thay đổi trong biến mục tiêu có thể gây ra sự chênh lệch lớn trong
trọng lượng tính toán. Trong những trường hợp như vậy, rất hữu ích để đặt một số nhất định
chính quy hóa (alpha) để giảm sự biến đổi này (tiếng ồn).

Khi alpha rất lớn, hiệu ứng chính quy chiếm ưu thế
hàm mất bình phương và các hệ số có xu hướng bằng không.
Ở cuối con đường, vì alpha có xu hướng về không
và giải pháp có xu hướng về các bình phương, hệ số nhỏ nhất
thể hiện dao động lớn. Trong thực tế cần phải điều chỉnh alpha
theo cách mà một sự cân bằng được duy trì giữa cả hai.
"""

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# X là ma trận Hilbert 10x10
X = 1. / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)

# ###################################################################################
# Tính toán đường dẫn

n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)

# ###################################################### ############################
# Hiển thị kết quả

ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim()[::-1])  # đảo ngược
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as function of the regularization')
plt.axis('tight')
plt.show()