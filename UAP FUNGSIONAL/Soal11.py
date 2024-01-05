def hitung_pangkat(pangkat):
    def pangkat_bilangan(bilangan):
        return bilangan ** pangkat
    return pangkat_bilangan

pangkat_dua = hitung_pangkat(2)
hasil_pangkat_dua = pangkat_dua(4)
print(hasil_pangkat_dua)  # 16

pangkat_tiga = hitung_pangkat(3)
hasil_pangkat_tiga = pangkat_tiga(3)
print(hasil_pangkat_tiga)  # 27