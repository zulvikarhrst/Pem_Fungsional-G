def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    # Inner function untuk menghitung nilai M
    def calculate_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    # Mendapatkan nilai M menggunakan inner function
    M = calculate_slope(p1, p2)

    # Mendapatkan nilai C
    def calculate_c(p):
        return p[1] - M * p[0]

    # Menghitung nilai C untuk kedua titik
    C1 = calculate_c(p1)
    C2 = calculate_c(p2)

    # Menggunakan rata-rata nilai C
    C = (C1 + C2) / 2

    return f"y = {M:.2f}x + {C:.2f}"

# Contoh penggunaan fungsi untuk NIM Ganjil (contoh: 1019)
print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(4, -2), point(-1, 3)))

# Perhitungan manual sesuai rumus untuk memverifikasi hasil
manual_M = (3 - (-2)) / (-1 - 4)
manual_C1 = -2 - manual_M * 4
manual_C2 = 3 - manual_M * (-1)
manual_C = (manual_C1 + manual_C2) / 2

manual_result = f"y = {manual_M:.2f}x + {manual_C:.2f}"
print("\nPerhitungan manual untuk memverifikasi hasil:")
print(manual_result)
