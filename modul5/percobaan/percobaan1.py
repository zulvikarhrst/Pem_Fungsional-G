import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Menentukan jenis garis dengan argumen 'linestyle'
plt.plot(xpoints, ypoints)  # Ganti 'dashed' dengan 'solid', 'dotted', atau jenis garis lainnya
plt.show()
