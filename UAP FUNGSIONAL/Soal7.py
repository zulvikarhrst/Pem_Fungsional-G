def kurang(a, b):
    return a - b

def sisagold(nim, a, b):
    if nim % 2 == 1:
        return kurang
    else: 
        return lambda x, y: kurang(y, x)

nim_ganjil = 13517001
nim_genap = 13517002

fungsi_ganjil = sisagold(nim_ganjil, 10, 5)
hasil_ganjil = fungsi_ganjil(10, 5)
print(hasil_ganjil) # 5

fungsi_genap = sisagold(nim_genap, 10, 5)
hasil_genap = fungsi_genap(10, 5)
print(hasil_genap)  # -5
