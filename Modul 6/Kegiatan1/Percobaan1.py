from PIL import Image, ImageDraw, ImageFont

gambarku = Image.open("C:/Users/Zulvikar Harist/Documents/Kuliah/SEMESTER 5/Pem. Fungsional/Modul 6/Kegiatan1/Background/UMMbg.jpg")
gambarBW = gambarku.convert("L")

draw = ImageDraw.Draw(gambarBW)
font_path = r"C:\Users\Zulvikar Harist\Documents\Kuliah\SEMESTER 5\Pem. Fungsional\Modul 6\Kegiatan1\Arial.ttf"
ukuran_font = 24

try:
    font = ImageFont.truetype(font_path, ukuran_font)
except IOError:
    print(f"Error loading font from {font_path}")
    font = ImageFont.load_default()

teks = "Nama : Zulvikar Harist\n NIM    : 202110370311033"

# membentuk ukuran kotak pembatas teks menggunakan objek font
kotak_teks = draw.textbbox((0, 0), teks, font=font)
lebar_teks, tinggi_teks = kotak_teks[2] - kotak_teks[0], kotak_teks[3] - kotak_teks[1]

# digunakan mengatur letak posisi teks
tengah_x = (gambarku.width - lebar_teks) // 2
tengah_y = (gambarku.height - tinggi_teks) // 20

draw.text((tengah_x, tengah_y), teks, font=font)

gambarBW.save("percobaan_satu.jpg")
gambarBW.show()
