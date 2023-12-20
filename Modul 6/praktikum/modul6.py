from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

def main():
    # Step 1: Buka kedua gambar menggunakan Pillow
    background_image = Image.open("C:/Users/Zulvikar Harist/Documents/Kuliah/SEMESTER 5/Pem. Fungsional/Modul 6/praktikum/Background/UMM.jpg")
    overlay_image = Image.open("C:/Users/Zulvikar Harist/Documents/Kuliah/SEMESTER 5/Pem. Fungsional/Modul 6/praktikum/Overlay/logo umm.png")

    # Step 2: Ubah gambar background menjadi hitam-putih, berotasi, dan blur
    background_image_bw = background_image.convert("L")  # Hitam-putih
    background_image_rotated = background_image_bw.rotate(30)  # Rotasi 30 derajat
    background_image_blurred = background_image_rotated.filter(ImageFilter.BLUR)  # Blur

    # Step 3: Ubah tingkat kecerahan dan kontras gambar overlay
    x, y = 33, 33  # Ganti dengan 2 digit NIM akhir Anda
    brightness_factor = 1.0 + x / 10.0
    contrast_factor = 1.0 + y / 10.0
    overlay_image_brightened = ImageEnhance.Brightness(overlay_image).enhance(brightness_factor)
    overlay_image_contrasted = ImageEnhance.Contrast(overlay_image_brightened).enhance(contrast_factor)

    # Resize sesuai kebutuhan (misalnya, ke ukuran maksimum 300x300)
    max_size = (300, 300)
    overlay_image_resized = overlay_image_contrasted.copy()
    overlay_image_resized.thumbnail(max_size)

    # Step 4: Sisipkan gambar overlay ke dalam gambar background
    x_center = (background_image.width - overlay_image_resized.width) // 2
    y_center = (background_image.height - overlay_image_resized.height) // 2
    background_image_final = background_image_blurred.copy()
    background_image_final.paste(overlay_image_resized, (x_center, y_center), overlay_image_resized)

    # Step 5: Tambahkan teks pada gambar overlay
    draw = ImageDraw.Draw(background_image_final)
    
    # Gunakan font default jika tidak ada Arial.ttf
    try:
        font = ImageFont.truetype("arial.ttf", 24)  # Gunakan huruf kecil pada "arial.ttf"
    except IOError:
        font = ImageFont.load_default()

    text = "Informatika JOSSS!"

    # Perhatikan perubahan di baris berikut
    text_size = draw.textbbox((0, 0), text, font=font)

    # Ubah nilai x_position dan y_position untuk menempatkan teks di bawah dan di tengah overlay
    x_position = (background_image_final.width - text_size[2] + text_size[0]) // 2
    y_position = overlay_image_resized.height + 10  # Jarak antara teks dan logo, bisa disesuaikan sesuai keinginan

    text_position = (x_position, y_position)
    draw.text(text_position, text, font=font, fill="white")

    # Step 6: Simpan gambar hasil edit
    background_image_final.save("tugas_praktikum_enam.jpg")

    # Tampilkan hasil edit
    background_image_final.show()

if __name__ == "__main__":
    main()
