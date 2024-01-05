import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox, Frame

# Tipe Data Sequence
tanggal = []
penonton = []

# Pure Function
def tambah_data(tgl, jml_penonton, data_tanggal, data_penonton):
    # Menambahkan data penonton harian ke list tanggal dan penonton
    data_tanggal.append(tgl)
    data_penonton.append(jml_penonton)

# Lambda Expression
hitung_rata_rata = lambda data: sum(data) / len(data) if len(data) > 0 else 0
# Lambda untuk menghitung rata-rata penonton, dengan perlakuan khusus jika data kosong

# Generator
def data_generator(data_tanggal, data_penonton):
    # Fungsi generator untuk menghasilkan pasangan (tanggal, penonton)
    for tgl, pen in zip(data_tanggal, data_penonton):
        yield tgl, pen

# Higher Order Function
def filter_data(minimal_penonton):
    # Fungsi higher-order untuk melakukan filtering berdasarkan minimal_penonton
    def inner_filter(data_tanggal, data_penonton):
        return [(tgl, pen) for tgl, pen in zip(data_tanggal, data_penonton) if pen >= minimal_penonton]
    return inner_filter

# Inner Function
def rata_rata_penonton(data_penonton):
    # Fungsi inner untuk mengembalikan fungsi rata-rata tanpa parameter
    def inner_rata_rata():
        return hitung_rata_rata(data_penonton)
    return inner_rata_rata

# Decorator
def log_kegiatan(func):
    # Decorator untuk mencetak pesan log setiap kali fungsi dipanggil
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Kegiatan selesai: {func.__name__}")
        return result
    return wrapper

@log_kegiatan
def tampilkan_grafik(data_tanggal, data_penonton):
    # Fungsi untuk menampilkan grafik menggunakan Matplotlib
    plt.plot(data_tanggal, data_penonton, marker='o')
    plt.title("Grafik Minat Menonton Bioskop")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Penonton")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# List Comprehension
penonton_diatas_rata = [pen for pen in penonton if pen > hitung_rata_rata(penonton)]
# List comprehension untuk mendapatkan daftar penonton di atas rata-rata

# Program Utama
def main():
    root = Tk()
    root.title("Program Minat Menonton Bioskop")

    frame1 = Frame(root)
    frame1.pack(pady=10)

    label = Label(frame1, text="Selamat datang di Program Minat Menonton Bioskop!")
    label.grid(row=0, column=0, columnspan=2)

    entry_tanggal = Entry(frame1, width=20)
    entry_tanggal.grid(row=1, column=0, padx=10)
    entry_tanggal.insert(0, "YYYY-MM-DD")

    entry_jml_penonton = Entry(frame1, width=20)
    entry_jml_penonton.grid(row=1, column=1, padx=10)
    entry_jml_penonton.insert(0, "Jumlah Penonton")

    def tambah_data_gui(tanggal, jml_penonton):
        try:
            jml_penonton_input = int(jml_penonton)
            tambah_data(tanggal, jml_penonton_input, tanggal, penonton)
            messagebox.showinfo("Info", "Data penonton berhasil ditambahkan.")
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah penonton dengan format numerik.")

    button_tambah_data = Button(frame1, text="Masukkan Data Penonton", command=lambda: tambah_data_gui(entry_tanggal.get(), entry_jml_penonton.get()))
    button_tambah_data.grid(row=2, column=0, columnspan=2, pady=10)

    frame2 = Frame(root)
    frame2.pack(pady=10)

    def tampilkan_grafik_gui():
        if not tanggal:
            messagebox.showwarning("Peringatan", "Belum ada data penonton. Silakan masukkan data terlebih dahulu.")
        else:
            tampilkan_grafik(tanggal, penonton)

    button_tampilkan_grafik = Button(frame2, text="Tampilkan Grafik", command=tampilkan_grafik_gui)
    button_tampilkan_grafik.grid(row=0, column=0, padx=10)

    def tampilkan_data_di_atas_rata_rata_gui():
        if not tanggal:
            messagebox.showwarning("Peringatan", "Tidak ada data penonton. Silakan masukkan data terlebih dahulu.")
        else:
            rata_rata = hitung_rata_rata(penonton)
            penonton_diatas_rata = [pen for pen in penonton if pen > rata_rata]

            if not penonton_diatas_rata:
                messagebox.showinfo("Info", "Tidak ada data penonton di atas rata-rata.")
            else:
                result = "Data penonton di atas rata-rata:\n"
                for tgl, pen in data_generator(tanggal, penonton):
                    if pen in penonton_diatas_rata:
                        result += f"{tgl}: {pen} penonton\n"

                messagebox.showinfo("Info", result)

    button_tampilkan_data_di_atas_rata_rata = Button(frame2, text="Tampilkan Data di Atas Rata-rata", command=tampilkan_data_di_atas_rata_rata_gui)
    button_tampilkan_data_di_atas_rata_rata.grid(row=0, column=1, padx=10)

    button_keluar = Button(root, text="Keluar", command=root.destroy)
    button_keluar.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
