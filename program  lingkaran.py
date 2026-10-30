import math
print("PROGRAM LINGKARAN")
print("1. Menghitung Keliling Lingkaran")
print("2. Menghitung Luas Lingkaran")
pilihan = int(input("Masukan pilihan (1/2): "))
jari = float(input("Masukan jari-jari: "))
if pilihan == 1:
    keliling = 2 * math.pi * jari
    print("Keliling lingkaran adalah:", keliling)
elif pilihan == 2:
    luas = math.pi * jari * jari
    print("Luas lingkaran adalah:",luas)
else:
    print("Pilihan tidak tersedia")