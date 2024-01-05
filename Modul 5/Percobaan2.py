import numpy as np
import matplotlib.pyplot as plt

# Data
data = {
    'main_line': {'x': [1, 7, 10], 'y': [4, 11, 6]},
    'additional_points': {'x': [3, 6, 9], 'y': [8, 5, 12]}
}

# Plot Garis Utama
plt.plot(data['main_line']['x'], data['main_line']['y'], color='red', marker='o', linestyle='-', linewidth=2, label='Garis Utama')

# Tambahkan Titik Tambahan
plt.scatter(data['additional_points']['x'], data['additional_points']['y'], color='blue', marker='x', label='Titik Tambahan')

# Batas Sumbu X & Y
plt.xlim([0, 15])
plt.ylim([0, 15])

# Judul & Label Sumbu
plt.title('Percobaan 2')
plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')

# Grid
plt.grid(True)

plt.legend()

# Anotasi Titik - Titik
for x, y in zip(data['main_line']['x'], data['main_line']['y']):
    plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Plot
plt.show()
