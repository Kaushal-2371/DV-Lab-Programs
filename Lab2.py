# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --------- #

# Load the dataset
df = sns.load_dataset("tips")

# Display first five rows
print(df.head())
# Check dataset information
df.info()
# Summary statistics
df.describe()

# --------- #

"""## Univariate Analysis"""

# Histogram - Total Bill

plt.figure(figsize=(8, 5))
sns.histplot(df["total_bill"], bins=20, kde=True, color="blue")
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Frequency")
plt.show()

# --------- #

# Boxplot - Tip

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["tip"], color="orange")
plt.title("Box Plot of Tips")
plt.ylabel("Tip Amount ($)")
plt.show()

# --------- #

"""## Bivariate Analysis"""

# Scatter Plot - Bill & Tip

plt.figure(figsize=(8, 5))
sns.scatterplot(x="total_bill", y="tip", data=df, hue="sex", style="smoker", palette="coolwarm")
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip Amount ($)")
plt.show()

# --------- #

# Box plot - Tips BY Day

plt.figure(figsize=(8, 5))
sns.boxplot(x="day", y="tip", data=df, palette="Set3")
plt.title("Tip Amounts by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip Amount ($)")
plt.show()

# --------- #

# Violin plot - Total Bill BY Gender

plt.figure(figsize=(8, 5))
sns.violinplot(x="sex", y="total_bill", data=df, palette="husl", inner="quartile")
plt.title("Distribution of Total Bill by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Bill ($)")
plt.show()

# --------- #

"""## Multivariate Analysis"""

# Pair plot

sns.pairplot(df, hue="sex", palette="husl")
plt.show()

# --------- #

# Heatmap

plt.figure(figsize=(8, 5))

# corr() can take only numeric values. so will filter only numeric values
numeric_df = df.select_dtypes(include=['float64', 'int64'])

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

