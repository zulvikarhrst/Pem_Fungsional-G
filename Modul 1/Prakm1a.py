class Peserta:
    def __init__(self, nama, nilai):
        self.id = None
        self.nama = nama
        self.nilai = nilai
        self.hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"

    def set_id(self, id):
        self.id = id

class SistemInformasiPeserta:
    def __init__(self):
        self.database_peserta = []
        self.next_id = 0

    def tambah_peserta(self):
        nama = input("Masukkan nama peserta: ")
        nilai = int(input("Masukkan nilai peserta: "))
        peserta = Peserta(nama, nilai)
        peserta.set_id(self.next_id)
        self.database_peserta.append(peserta)
        self.next_id += 1
        print("Peserta berhasil ditambahkan!")

    def edit_nilai(self):
        if not self.database_peserta:
            print("Database peserta masih kosong.")
            return

        print("Daftar Peserta:")
        for peserta in self.database_peserta:
            print(f"ID: {peserta.id}, Nama: {peserta.nama}, Nilai: {peserta.nilai}, Hasil Akhir: {peserta.hasil_akhir}")

        try:
            id_peserta = int(input("Masukkan ID peserta yang ingin diedit: "))
            for peserta in self.database_peserta:
                if peserta.id == id_peserta:
                    new_nilai = int(input("Masukkan nilai baru: "))
                    peserta.nilai = new_nilai
                    peserta.hasil_akhir = "Lolos" if new_nilai >= 75 else "Tidak Lolos"
                    print("Nilai peserta berhasil diubah!")
                    return
            print("ID peserta tidak ditemukan.")
        except ValueError:
            print("Masukkan angka yang valid untuk ID dan nilai.")

    def lihat_nilai_dan_hasil(self, id_peserta):
        for peserta in self.database_peserta:
            if peserta.id == id_peserta:
                print(f"Nama: {peserta.nama}, Nilai: {peserta.nilai}, Hasil Akhir: {peserta.hasil_akhir}")
                return
        print("ID peserta tidak ditemukan.")

    def run(self):
        while True:
            print("\n=== Sistem Informasi Peserta ===")
            print("1. Admin - Tambah Peserta")
            print("2. Admin - Edit Nilai Peserta")
            print("3. Peserta - Lihat Nilai dan Hasil Akhir")
            print("4. Keluar")

            peran = input("Pilih Menu (Admin/Peserta/Keluar): ").lower()

            if peran == "admin":
                print("\n=== Halaman Admin ===")
                print("1. Tambah Peserta")
                print("2. Edit Nilai Peserta")
                admin_pilihan = input("Pilih tindakan (1/2): ")
                if admin_pilihan == "1":
                    self.tambah_peserta()
                elif admin_pilihan == "2":
                    self.edit_nilai()
                else:
                    print("Pilihan tidak valid.")
            elif peran == "peserta":
                try:
                    id_peserta = int(input("Masukkan ID Anda: "))
                    self.lihat_nilai_dan_hasil(id_peserta)
                except ValueError:
                    print("Masukkan ID yang valid.")
            elif peran == "keluar":
                print("Terima kasih, program selesai.")
                break
            else:
                print("Pilihan peran tidak valid. Silakan pilih Admin, Peserta, atau Keluar.")

# Jalankan program
if __name__ == "__main__":
    sistem_informasi_peserta = SistemInformasiPeserta()
    sistem_informasi_peserta.run()
