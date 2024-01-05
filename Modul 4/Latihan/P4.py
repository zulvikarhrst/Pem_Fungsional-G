import math

def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        x_baru = x + tx
        y_baru = y + ty
        return (x_baru, y_baru)
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        x_baru = x * sx
        y_baru = y * sy
        return (x_baru, y_baru)
    return transformasi

def rotasi(sudut):
    def transformasi(p):
        x, y = p
        sudut_radian = math.radians(sudut)
        x_baru = x * math.cos(sudut_radian) - y * math.sin(sudut_radian)
        y_baru = x * math.sin(sudut_radian) + y * math.cos(sudut_radian)
        return (x_baru, y_baru)
    return transformasi

# Titik awal
titik_P = (3, 5)

# Translasi
translasi_func = translasi(2, -1)
titik_setelah_translasi = translasi_func(titik_P)
print(f"Koordinat setelah translasi: {titik_setelah_translasi}")

# Dilatasi
dilatasi_func = dilatasi(2, -1)
titik_setelah_dilatasi = dilatasi_func(titik_P)
print(f"Koordinat setelah dilatasi: {titik_setelah_dilatasi}")

# Rotasi
rotasi_func = rotasi(30)
titik_setelah_rotasi = rotasi_func(titik_P)
print(f"Koordinat setelah rotasi: {titik_setelah_rotasi}")