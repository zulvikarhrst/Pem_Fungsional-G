import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Membuat 1000 sampel normal dengan rata-rata 50 dan standar deviasi 5
sample = np.random.normal(loc=50, scale=5, size=1000)

# Menampilkan sampel dalam bentuk histogram
plt.figure(figsize=(5, 4))
plt.hist(sample, bins=10, density=True)
plt.show()

# Menghitung mean dan standar deviasi sampel
sample_mean = np.mean(sample)
sample_std = np.std(sample)
print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

# Mendefinisikan distribusi normal dengan mean dan standar deviasi dari sampel
dist = norm(sample_mean, sample_std)

# Membuat list nilai untuk perhitungan distribusi probabilitas
values = [value for value in range(30, 70)]

# Menghitung probabilitas distribusi berdasarkan nilai yang telah disiapkan
probabilities = [dist.pdf(value) for value in values]

# Menampilkan histogram sampel dan plot distribusi probabilitas
plt.hist(sample, bins=10, density=True)
plt.plot(values, probabilities)
plt.legend()
plt.show()
