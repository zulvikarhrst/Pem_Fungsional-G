ganjil = [x for x in range(51) if x % 2 != 0]
kelipatan_tiga = [x for x in ganjil if x % 3 == 0]

print(kelipatan_tiga)