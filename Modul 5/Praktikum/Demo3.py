import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def visualisasi_histogram(data, interval, kurva_pdf=None):# membuat histogram dari data tinggi badan.
    plt.hist(data, bins=interval, edgecolor='black', alpha=0.7, density=False, label='Data')
    plt.title('Histogram Frekuensi Tinggi Badan')
    plt.xlabel('Interval Tinggi Badan (cm)')
    plt.ylabel('Frekuensi')

    if kurva_pdf is not None:
        plt.plot(kurva_pdf[0], kurva_pdf[1], color='red', label='PDF (Normal Distribution)')

    plt.legend(loc='lower left')
    plt.show()

def main():
    data_tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
    interval = [150, 160, 170, 180, 190]

    frekuensi, batas_interval = np.histogram(data_tinggi_badan, bins=interval)

    mean, std_dev = np.mean(data_tinggi_badan), np.std(data_tinggi_badan)
    kurva_pdf_x = np.linspace(min(data_tinggi_badan), max(data_tinggi_badan), 100)
    kurva_pdf_y = norm.pdf(kurva_pdf_x, mean, std_dev) * len(data_tinggi_badan) * (batas_interval[1] - batas_interval[0])
    kurva_pdf = (kurva_pdf_x, kurva_pdf_y)

    visualisasi_histogram(data_tinggi_badan, interval, kurva_pdf)

if __name__ == "__main__":
    main()
