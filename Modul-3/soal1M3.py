jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    try:
        jarak = int(input("Masukkan jarak penumpang (km), 0 untuk selesai: "))
    except :
        print("Input tidak valid, masukkan angka bulat.")
        continue

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak negatif tidak valid, ulangi.")
        continue

    jumlah_penumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000 * (jarak - 5)
    else:
        tarif = 13000 + 500 * (jarak - 15)

    if jumlah_penumpang % 5 == 0:
        tarif *= 0.5
        print(f"Penumpang ke-{jumlah_penumpang}: diskon 50%")

    print(f"Tarif: Rp{tarif:}")

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("\n=== Rekap ===")
print(f"Jumlah penumpang : {jumlah_penumpang}")
print(f"Total pendapatan : Rp{total_pendapatan}")
if jumlah_penumpang > 0:
    print(f"Jarak terjauh    : {jarak_terjauh} km")
    print(f"Rata-rata jarak  : {total_jarak / jumlah_penumpang} km")
else:
    print("Tidak ada penumpang.")