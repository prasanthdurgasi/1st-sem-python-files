import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.DataFrame({
    'feature1': [10, 15, 16, 20, 23, 40, 45, 47, 50],
    'feature2': [12, 16, 17, 21, 23, 43, 48, 49, 50]
})
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)
data['Cluster'] = kmeans.labels_
centroids = kmeans.cluster_centers_
mstd = data.groupby('Cluster').agg(['mean', 'std'])
print(mstd)
plt.scatter(data['feature1'], data['feature2'], c=data['Cluster'], cmap='viridis', label='Data Points')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='o', color='red', s=200, label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
