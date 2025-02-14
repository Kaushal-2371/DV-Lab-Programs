# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.preprocessing import StandardScaler
import folium
from folium.plugins import MarkerCluster

# Load the iris dataset
df = sns.load_dataset("iris")
# Display first five rows
df.head()

# --------- #

# Box Plot
# Creating boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x=df["sepal_length"])
plt.title("Box plot of sepal length")
plt.show()

# --------- #

# Identifier the outlier using IQR method
q1 = df["sepal_length"].quantile(0.25)
q3 = df["sepal_length"].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print()

outliers = df[(df["sepal_length"] < lower_bound) | (df["sepal_length"] > upper_bound)]
print("Outliers:")
print(outliers)

# --------- #

# Now will treat the outliers
df["sepal_length"] = np.where(df["sepal_length"] > upper_bound, upper_bound,np.where(df["sepal_length"] < lower_bound, lower_bound, df["sepal_length"]))

plt.figure(figsize=(8,5))
sns.boxplot(x=df["sepal_length"])
plt.title("Box plot after outlier treatment")
plt.show()

# --------- #

# making heatmap
corr_matrix = df.drop(columns = ["species"]).corr()

# Create a heatmap
plt.figure(figsize=(8,5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# --------- #

# Dendogram
# Standardizing the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.drop(columns = ["species"]))

# Generating dendogram
plt.figure(figsize = (10,5))
sch.dendrogram(sch.linkage(df_scaled, method="ward"))
plt.title("dendogram for hierarchical clustering")
plt.xlabel("data points")
plt.ylabel("euclidean distance")
plt.show()

sns.pairplot(df, hue = "species", palette = "husl")
plt.show()

# --------- #

# For geographical visualization, we use a Point Map.
# Sample latitude and longitude points (random example)
location_data = pd.DataFrame({
    'latitude': [28.6139, 19.0760, 12.9716, 22.5726, 13.0827],  # Location in India
    'longitude': [77.2090, 72.8777, 77.5946, 88.3639, 80.2707],
    'city': ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai']
})

# Create map centered at an average location
m = folium.Map(location=[20, 78], zoom_start=5)

# Add markers
marker_cluster = MarkerCluster().add_to(m)
for idx, row in location_data.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['city']).add_to(marker_cluster)

# Display the map
m