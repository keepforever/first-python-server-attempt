import numpy as np
import pandas as pd
import pickle

import matplotlib.pyplot as plt

import sklearn
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report


iris = datasets.load_iris()

X = scale(iris.data)
print (X)
y = pd.DataFrame(iris.target)
variable_names = iris.feature_names

clustering = KMeans(n_clusters=3, random_state=5)

clustering.fit(X)

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(clustering, open(filename, 'wb'))



