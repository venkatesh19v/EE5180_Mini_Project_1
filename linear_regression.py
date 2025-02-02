# -*- coding: utf-8 -*-
"""linear_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14cfbknM6nNaiBkxPNVloVbxokm1OurBG
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('song_data.csv')

# Compute the correlation matrix
correlation_matrix = data.corr()

# Plot the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Features')
plt.xlabel('Features')
plt.ylabel('Features')
plt.show()

# Step 3: Identify features most correlated with 'energy'

correlation_with_target = correlation_matrix['energy'].sort_values(ascending=False)
print("Features correlated with 'energy':\n", correlation_with_target)

# Step 4: Pair plots and histograms for top correlated features

top_features = correlation_with_target.index[1:6]  # Select the top 5 features
print("Top features for visualization:\n", top_features)

# # Pair plot for selected features
# pair_plot = sns.pairplot(data[top_features], diag_kind='kde')

# # Manually set the title for each subplot
# plt.subplots_adjust(top=0.9)  # Adjust top to make room for the main title
# plt.suptitle('Pair Plots of Top Correlated Features', fontsize=16)

# # Set the axis labels for each subplot
# for ax in pair_plot.axes.flatten():
#     ax.set_xlabel(ax.get_xlabel() + ' (feature)', fontsize=10)
#     ax.set_ylabel(ax.get_ylabel() + ' (feature)', fontsize=10)
#     ax.set_title('', fontsize=12)  # Clear default titles to avoid overlap

# plt.show()

# # Plot histograms of the top correlated features
# data[top_features].hist(bins=15, figsize=(15, 10), layout=(2, 3))
# plt.suptitle('Histograms of Top Correlated Features', y=1.02)
# for ax in plt.gcf().axes:
#     ax.set_xlabel('Feature Value')
#     ax.set_ylabel('Frequency')
# plt.show()

# Step 5: Feature selection and scaling for training
selected_features = top_features.tolist()  # Convert to a list for selection
X = data[selected_features]  # Use the selected features
y = data['energy']           # Target variable

# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler on the features and transform them
X_scaled = scaler.fit_transform(X)

# Step 6: Split the data into training and testing sets (using the scaled features)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 7: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 9: Evaluate the model

mse = np.mean((y_test - y_pred) ** 2)

# Calculate R-squared using scikit-learn's r2_score function
r2 = r2_score(y_test, y_pred)

# Display the evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("R-squared:", r2)

# Display the model's coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predicted vs. Actual Plot
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='b')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Energy')
plt.ylabel('Predicted Energy')
plt.title('Predicted vs. Actual Energy')
plt.show()

# Residual Plot
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.6, color='r')
plt.axhline(y=0, color='k', linestyle='--', lw=2)
plt.xlabel('Predicted Energy')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()