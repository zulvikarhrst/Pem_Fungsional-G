import matplotlib.pyplot as plt
import numpy as np

# Data 3 Garis
data = {
    'Garis 1': np.array([3, 8, 1, 10]),
    'Garis 2': np.array([6, 2, 7, 11]),
    'Garis 3': np.array([5, 12, 4, 9])
}

# Plot Garis Warna Berbeda
for label, y_values in data.items():
    marker = 'o' if label == 'Garis 1' else 's' if label == 'Garis 2' else '^'
    linestyle = '-' if label == 'Garis 1' else '--' if label == 'Garis 2' else ':'
    color = 'black' if label == 'Garis 1' else 'purple' if label == 'Garis 2' else 'red'
    
    plt.plot(y_values, label=label, marker=marker, linestyle=linestyle, color=color)

# Judul & Label Sumbu
plt.title('Percobaan 3')
plt.xlabel('Indeks Data')
plt.ylabel('Nilai Y')

plt.legend()

# Plot
plt.show()
