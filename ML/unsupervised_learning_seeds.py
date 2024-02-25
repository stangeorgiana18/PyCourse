import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cols = ['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry', 'groove', 'class']
df = pd.read_csv('seeds_dataset.txt', names = cols, sep = '\s+') # any spaces recognized as space separators

#print(df.head())

for i in range(len(cols) - 1):
    for j in range(i + 1, len(cols) - 1):
        x_label = cols[i]
        y_label = cols[j]
        sns.scatterplot(x = x_label, y = y_label, data = df, hue = 'class')
        plt.show()

# CLUSTERING
        
from sklearn.cluster import KMeans

x = "perimeter"
y = 'asymmetry'
X = df[[x, y]].values # extract specific values

kmneans = KMeans(n_clusters = 3).fit(X)
clusters = kmneans.labels_ # predictions for the clusters 

print(clusters)
print(df['class'].values)

cluster_df = pd.DataFrame(np.hstack((X, clusters.reshape(-1, 1))), columns = [x, y, 'class'])

## ORIGINAL CLASSES
sns.scatterplot(x = x, y = y, hue = 'class', data = cluster_df)
plt.plot()
plt.show()

## K-MEANS CLASSES 
sns.scatterplot(x = x, y = y, hue = 'class', data = cluster_df)
plt.plot()
plt.show() # notice the clusters are similar between the orginal and kmc classes 


# HIGHER DIMENSIONS

X = df[cols[:-1]].values # all the columns, except for the class

kmeans = KMeans(n_clusters = 3).fit(X)
cluster_df = pd.DataFrame(np.hstack((X, kmeans.labels_.reshape(-1, 1))), columns = df.columns)

# K Means classes
sns.scatterplot(x = x, y = y, hue = 'class', data = cluster_df)
plt.plot()
plt.show()

# Original classes
sns.scatterplot(x = x, y = y, hue = 'class', data = df)
plt.plot()
plt.show()

