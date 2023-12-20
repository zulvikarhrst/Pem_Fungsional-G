from PIL import Image

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open("C:/Users/Zulvikar Harist/Documents/Kuliah/SEMESTER 5/Pem. Fungsional/Modul 6/Kegiatan2/Background/UMMbg.jpg")
overlay_image = Image.open("C:/Users/Zulvikar Harist/Documents/Kuliah/SEMESTER 5/Pem. Fungsional/Modul 6/Kegiatan2/Overlay/logo umm.png")

# TODO 2: Periksa apakah overlay image memiliki alpha channel
if 'A' in overlay_image.getbands():
    alpha = overlay_image.split()[3]
    #overlay_image = overlay_image.convert('RGB')
    overlay_image.putalpha(alpha)

# TODO 3: (optional) Perkecil ukuran gambar overlay menggunakan method resize()
max_size = (300, 300)
overlay_image.thumbnail(max_size)

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 23

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center), overlay_image)

# TODO 5: Simpan gambar hasil edit
background_image.save("hasil_edit.jpg")

# TODO 6: Tampilkan
background_image.show()
