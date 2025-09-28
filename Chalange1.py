def hitung_total(harga, jumlah, diskon=0):
    total = harga * jumlah
    if diskon > 0:
        potongan = total * (diskon / 100)
        total = total - potongan
    return total

harga = int(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))
diskon = int(input("Masukkan diskon (%): "))

total_belanja = hitung_total(harga, jumlah, diskon)
print("Total Belanja = ", total_belanja)