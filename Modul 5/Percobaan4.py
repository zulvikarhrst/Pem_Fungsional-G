import matplotlib.pyplot as plt
import numpy as np

# Data Scatter Plot
data_scatter = {'x': [1, 2, 3, 4, 5], 'y': [4, 8, 3, 9, 7]}
colors = ['black', 'red', 'blue', 'yellow', 'orange']
sizes = [150, 200, 250, 300, 350]

# Scatter Plot Warna & Ukuran Marker
plt.scatter(data_scatter['x'], data_scatter['y'], c=colors, s=sizes, alpha=0.7, edgecolors='black', linewidth=2, label='Data Points')

# Judul & Label Sumbu
plt.title('Percobaan 4')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

plt.legend()

plt.show()
