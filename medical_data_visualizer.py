import pandas as pd
import matplotlib.pyplot as plt

# Load medical data from CSV
data = pd.read_csv('medical_data.csv')

# Show first few rows
print(data.head())

# Visualize: Example - Age distribution
plt.hist(data['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()

# Visualize: Example - Cholesterol levels
plt.scatter(data['age'], data['cholesterol'], color='green', alpha=0.5)
plt.title('Cholesterol vs Age')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.show()