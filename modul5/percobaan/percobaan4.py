import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Scatter plot dengan gaya penanda yang diperbaiki
warna = ['red', 'green', 'blue', 'orange', 'purple']
ukuran = [50, 100, 150, 200, 250]
penanda = 'o'  # Gaya penanda yang digunakan untuk semua titik

plt.scatter(x, y, c=warna, s=ukuran, marker=penanda, alpha=0.7, label='Titik Data')

# Menambahkan label sumbu
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan judul
plt.title('Scatter Plot dengan Variasi')

# Menampilkan legenda
plt.legend()

# Menampilkan plot
plt.show()
