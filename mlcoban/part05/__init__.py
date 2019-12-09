import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import normalize
from display_network import *

(XTrain, yTrain), (XTest, yTest) = mnist.load_data()

X0 = np.asarray(XTest)[:1000, :]/256
X = X0

K = 10
kmeans = KMeans(n_clusters=K).fit(X)

pred_label = kmeans.predict(X)
