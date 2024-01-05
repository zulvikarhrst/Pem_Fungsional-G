from functools import reduce

data_angka = [3, 9, 15, 21, 27, 33, 39, 45]

hasil_penjumlahan = reduce(lambda x, y: x + y, data_angka)
print(hasil_penjumlahan)