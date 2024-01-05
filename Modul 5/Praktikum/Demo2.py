import matplotlib.pyplot as plt

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# Ekstrak harga produk dan jumlah produk terjual
harga_produk = list(map(lambda x: x[1], data_transaksi))
jumlah_terjual = list(map(lambda x: x[2], data_transaksi))

# Scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(10, 5))
plt.scatter(harga_produk, jumlah_terjual, color='deeppink', label='Data Transaksi')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')
plt.legend()
plt.show()

# Hitung total pendapatan untuk setiap produk
total_pendapatan = list(map(lambda x: x[1] * x[2], data_transaksi))

# Bar chart untuk menyajikan pendapatan produk
produk_names = list(map(lambda x: x[0], data_transaksi))
plt.figure(figsize=(10, 5))
plt.bar(produk_names, total_pendapatan, color='purple', label='Pendapatan')
plt.title('Pendapatan Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan Produk')
plt.legend()
plt.show()
