# Joshua Potter, jop13

''' This program demostrates clustering on the iris dataset
    The iris dataset is a dataset about 3 kinds of iris flowers, with 4 features
    per flower. 
    Clustering is a type of machine learning where there is no idea of the ground 
    truth. Instead, data points are grouped as "similar" based on how close
    they are to each other.

    The sklearn library contains a lot of functions for machine learning,
    including clustering '''

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

# The sklearn library come prepackaged with a bunch of datasets. We are loading the iris dataset

digits = datasets.load_digits()

pca = PCA(n_components=2)
digits.data = pca.fit_transform(digits.data)

''' pandas is a library that organizes data nicely. We are formatting the
    dataset into a pandas dataframe. Then we name the features. '''

x = pd.DataFrame(digits.data)
x.columns = ['Petal_L', 'Petal_W']

''' Though clustering does not require the ground truth, the dataset is 
    labeled anyway. So we can check the results of clustering against the answer.
    So, we load the 'answer' into a separate data frame '''

y = pd.DataFrame(digits.target)
y.columns = ['Targets']

# this line actually builds the machine learning model and runs the algorithm
# on the dataset
model = KMeans(n_clusters =10)
model.fit(x)

#plot the 2 graphs side to side
plt.figure(111)

colormap = np.array(['darkred', 'red', 'darkblue', 'blue', 'green', 'lawngreen', 'yellow', 'orange', 'purple', 'black'])
 
# Plot the Models Classifications
plt.scatter(x.Petal_L, x.Petal_W, c=colormap[model.labels_], s=40)
plt.title('K Means Classification')

plt.show()
