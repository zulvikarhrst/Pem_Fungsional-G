# Inisialisasi database peserta
database_peserta = []

# Fungsi untuk menambah peserta oleh admin
tambah_peserta = lambda id, nama, nilai: database_peserta.append({"ID": id, "Nama": nama, "Nilai": nilai, "Hasil Akhir": "Lolos" if nilai >= 75 else "Tidak Lolos"})

# Fungsi untuk mengedit nilai oleh admin
edit_nilai = lambda id, nilai: next((peserta.update({"Nilai": nilai, "Hasil Akhir": "Lolos" if nilai >= 75 else "Tidak Lolos"}) for peserta in database_peserta if peserta["ID"] == id), None)

# Fungsi untuk mencari peserta berdasarkan ID
find_peserta = lambda id: next((p for p in database_peserta if p["ID"] == id), None)

# Fungsi untuk mencari peserta berdasarkan nama
find_peserta_by_name = lambda nama: [p for p in database_peserta if p["Nama"].lower() == nama.lower()]

# Fungsi untuk menampilkan hasil akhir peserta oleh peserta
tampilkan_hasil_peserta = lambda id: print_result(id)

def print_result(id):
    peserta = find_peserta(id)
    if peserta:
        print("Nama: {}".format(peserta["Nama"]))
        print("Nilai: {}".format(peserta["Nilai"]))
        print("Hasil Akhir: {}".format(peserta["Hasil Akhir"]))
    else:
        print("ID peserta tidak ditemukan.")

# Program utama
while True:
    print("Selamat datang di Sistem Informasi Peserta")
    print("1. Login sebagai Admin")
    print("2. Login sebagai Peserta")
    print("3. Keluar")

    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        print("Login sebagai Admin")
        username = input("Username: ")
        password = input("Password: ")
        # Anda dapat menambahkan validasi admin di sini

        while True:
            print("\nMenu Admin:")
            print("1. Tambah Peserta")
            print("2. Edit Nilai Peserta")
            print("3. Cari Peserta")
            print("4. Lihat Data Peserta")
            print("5. Keluar")

            admin_pilihan = input("Pilih opsi: ")

            if admin_pilihan == "1":
                nama = input("Nama Peserta: ")
                nilai = int(input("Nilai Peserta: "))
                tambah_peserta(len(database_peserta), nama, nilai)
            elif admin_pilihan == "2":
                id = int(input("ID Peserta: "))
                nilai = int(input("Nilai Baru: "))
                edit_nilai(id, nilai)
            elif admin_pilihan == "3":
                cari_nama = input("Nama Peserta yang dicari: ")
                hasil_pencarian = find_peserta_by_name(cari_nama)
                if hasil_pencarian:
                    print("Hasil Pencarian:")
                    for peserta in hasil_pencarian:
                        print("ID: {}, Nama: {}, Nilai: {}, Hasil Akhir: {}".format(
                            peserta["ID"], peserta["Nama"], peserta["Nilai"], peserta["Hasil Akhir"]
                        ))
                else:
                    print("Peserta tidak ditemukan.")
            elif admin_pilihan == "4":
                print("\nData Peserta:")
                for peserta in database_peserta:
                    print("ID: {}, Nama: {}, Nilai: {}, Hasil Akhir: {}".format(
                        peserta["ID"], peserta["Nama"], peserta["Nilai"], peserta["Hasil Akhir"]
                    ))
            elif admin_pilihan == "5":
                break
            else:
                print("Pilihan tidak valid.")
    elif pilihan == "2":
        print("Login sebagai Peserta")
        id = int(input("Masukkan ID Anda: "))
        tampilkan_hasil_peserta(id)
    elif pilihan == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")