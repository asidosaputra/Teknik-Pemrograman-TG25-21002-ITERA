import konversi;

print("Pilih konversi:")
print("1. Celcius ke Fahrenheit")
print("2. Fahrenheit ke Celcius")

pilih = int(input("Masukkan pilihan (1/2): "))

if pilih == 1:
    c = float(input("Masukkan suhu Celcius: "))
    hasil = konversi.c_to_f(c)
    print("Suhu dalam Fahrenheit = ", hasil)
elif pilih == 2:
    f = float(input("Masukkan suhu Fahrenheit: "))
    hasil = konversi.f_to_c(f)
    print("Suhu dalam Celcius = ", hasil)
else:
    print("Pilihan tidak valid!")