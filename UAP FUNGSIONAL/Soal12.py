def kalimat_hasil_prima_decorator(func):
    def wrapper(angka):
        if func(angka):
            return "Benar"
        else:
            return "Salah"
    return wrapper

@kalimat_hasil_prima_decorator
def is_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

hasil = is_prima(13)
print(hasil)