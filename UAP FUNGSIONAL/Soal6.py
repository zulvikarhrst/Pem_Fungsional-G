ganjil_generator = (x for x in range(51) if x % 2 != 0)

for angka in ganjil_generator:
    print(angka)