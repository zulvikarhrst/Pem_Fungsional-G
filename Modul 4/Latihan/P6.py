def point(x, y):
    return x, y

def line_equation_of(p1, M):
    # Menghitung nilai C menggunakan rumus y - y1 = m(x - x1)
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

# Contoh penggunaan fungsi untuk NIM Ganjil (contoh: 033)
print("Persamaan garis yang melalui titik (6, -2) dan bergradien 2:")
print(line_equation_of(point(0, 3), 3))
