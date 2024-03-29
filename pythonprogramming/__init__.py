import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100)

print(len(digits.data))

X, y = digits.data[:-10], digits.target[:-10]
clf.fit(X, y)

testValue = -6
print('Prediction', clf.predict([digits.data[testValue]]))
plt.imshow(digits.images[testValue], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
