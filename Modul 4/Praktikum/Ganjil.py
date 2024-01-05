import math

def point(x, y):
    return x, y

def line_equation_of(p1, M, C):
    return f"y = {M:.2f}x + {C:.2f}"

def transformation_decorator(func):
    def wrapper():
        # Meminta input dari pengguna
        x = float(input("Masukkan nilai x untuk titik A: "))
        y = float(input("Masukkan nilai y untuk titik A: "))
        gradient_original = float(input("Masukkan nilai gradien awal: "))

        # Menambahkan input untuk transformasi
        tx = float(input("Masukkan nilai tx untuk translasi: "))
        ty = float(input("Masukkan nilai ty untuk translasi: "))
        angle = float(input("Masukkan nilai rotasi (dalam derajat): "))
        sx = float(input("Masukkan nilai sx untuk dilatasi secara horizontal: "))
        sy = float(input("Masukkan nilai sy untuk dilatasi secara vertikal: "))

        # Memanggil fungsi transformasi yang sebenarnya
        func(point(x, y), gradient_original, tx, ty, angle, sx, sy)

    return wrapper

@transformation_decorator
def transformations(A, gradient_original, tx, ty, angle, sx, sy):
    def translate(x, y, tx, ty):
        return x + tx, y + ty

    def dilate(x, y, sx, sy):
        return x * sx, y * sy

    def rotate(x, y, angle):
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        sin_val = math.sin(angle_rad)
        return x * cos_val - y * sin_val, x * sin_val + y * cos_val

    # Translasi
    A_translated = translate(A[0], A[1], tx, ty)

    # Rotasi
    A_rotated = rotate(A_translated[0], A_translated[1], angle)

    # Dilatasi3
    A_transformed = dilate(A_rotated[0], A_rotated[1], sx, sy)

    # Menghitung gradien hasil transformasi
    gradient_transformed = gradient_original

    # Menghitung intercept hasil transformasi
    intercept_transformed = A_transformed[1] - gradient_transformed * A_transformed[0]

    # Menampilkan hasil transformasi
    print("\nHasil transformasi:")
    print("Persamaan garis yang melalui titik awal:")
    print(line_equation_of(A, gradient_original, -gradient_original * A[0] + A[1]))

    print("\nPersamaan garis baru setelah transformasi:")
    print(line_equation_of(point(A_transformed[0], A_transformed[1]), gradient_transformed, intercept_transformed))

# Memanggil fungsi utama
transformations()