import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Daftar Nilai
values = list(range(30, 70))

# Membuat Sample Data Dengan Distribusi Normal
sample = np.random.normal(loc=50, scale=5, size=1000)

# Menampilkan Dalam Bentuk Histogram & Kurva Distribusi Normal Pada Satu Plot
plt.figure(figsize=(8, 6))

# Histogram
plt.hist(sample, bins=20, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Histogram')

# Menghitung Mean & Standard Deviation
sample_mean = np.mean(sample)
sample_std = np.std(sample)

# Membuat Objek Distribusi Normal
dist = norm(sample_mean, sample_std)

# Menghitung Probabilitas Menggunakan Metode PDF
probabilities = dist.pdf(values)

# Kurva Distribusi Normal
plt.plot(values, probabilities, label='Distribusi Normal', color='red', linewidth=2)

# Judul & Label Sumbu
plt.title('Percobaan 5')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi Relatif / Probabilitas')

plt.legend()

plt.show()
