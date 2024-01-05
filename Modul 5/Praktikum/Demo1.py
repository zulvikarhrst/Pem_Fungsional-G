from functools import reduce
import matplotlib.pyplot as plt

# Data nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Fungsi untuk menghitung rata-rata
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis
label_mahasiswa = list(map(lambda x: f"{x+1}", range(len(nilai_mahasiswa))))

# Visualisasi data dalam bentuk diagram batang
plt.bar(label_mahasiswa, nilai_mahasiswa, color='blue', label='Nilai Mahasiswa')
plt.axhline(y=rata_rata, color='red', linestyle='--', label=f'Rata-rata = {rata_rata:.2f}')

# Menambahkan keterangan di pojok kanan atas
plt.legend()
plt.title('Diagram Batang Nilai Mahasiswa')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')

# Menambahkan keterangan (simbol garis patah-patah) rata-rata 
plt.annotate(f'Rata-rata = {rata_rata:.2f}', xy=(1, 1), xytext=(-70, -20),
             xycoords='axes fraction', textcoords='offset points',
             ha='right', va='top', bbox=dict(boxstyle='round,pad=0.3', edgecolor='red', facecolor='white'))

# Menampilkan diagram
plt.show()
