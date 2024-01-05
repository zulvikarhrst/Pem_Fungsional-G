# TODO 1 : Tambahkan Library yang dibutuhkan
import matplotlib.pyplot as plt

# Setiap tupel berisi informasi sebagai berikut:
# (jenis_kendaraan, penggunaan_energi_per_km, biaya_operasional_per_km)
data = [
    ('Bus', 5, 200),
    ('Trem', 8, 150),
    ('Kereta', 12, 300),
    ('Minibus', 6, 180),
    ('Tram', 9, 220)
]

# TODO 2 : Pisahkan data masing-masing (dapat menggunakan pemetaan)
jenis_kendaraan, penggunaan_energi, biaya_operasional = zip(*data)

# TODO 3 : Lengkapi kode untuk visualisasi data penggunaan energi
plt.subplot(1, 3, 1)
plt.bar(jenis_kendaraan, penggunaan_energi, color='blue')
plt.title('Penggunaan Energi per km')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Penggunaan Energi per km')

# TODO 4 : Lengkapi kode untuk visualisasi data biaya operasional
plt.subplot(1, 3, 2)
plt.bar(jenis_kendaraan, biaya_operasional, color='blue')
plt.title('Biaya Operasional per km')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Biaya Operasional per km')

# TODO 6 : Lengkapi kode untuk menggambar scatter plot
# TODO 7 : Memberikan label pada tiap titik
plt.subplot(1, 3, 3)
plt.scatter(penggunaan_energi, biaya_operasional, color='blue', label='Jenis Kendaraan')
for i, kendaraan in enumerate(jenis_kendaraan):
    plt.text(penggunaan_energi[i], biaya_operasional[i], kendaraan, fontsize=8, ha='right', va='bottom')

# Menambahkan Legenda
plt.legend()

# Tampilkan Plot
plt.tight_layout()
plt.show()