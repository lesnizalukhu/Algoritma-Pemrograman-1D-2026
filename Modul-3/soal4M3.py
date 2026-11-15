JUMLAH_MAHASISWA = 10
KUOTA_PENUH = 3

penuh = 0
sebagian = 0
tidak_dapat = 0
tidak_memenuhi = 0
diproses = 0

for i in range(1, JUMLAH_MAHASISWA + 1):
    print(f"\n--- Mahasiswa ke-{i} ---")
    nama = input("Nama : ")

    while True:
        teks = input("IPK : ").replace(",", ".")
        if not teks.replace(".", "", 1).isdigit():
            print("Input tidak valid, masukkan angka.")
            continue
        ipk = float(teks)
        if ipk <= 4:
            break
        print("IPK harus antara 0 sampai 4.")

    while True:
        teks = input("Penghasilan orang tua (Rp): ")
        if teks.isdigit():
            penghasilan = int(teks)
            break
        print("Input tidak valid, masukkan angka bulat tanpa titik/koma.")

    diproses += 1

    if ipk < 3.00:
        print(f"{nama}: TIDAK MEMENUHI SYARAT (IPK < 3,00)")
        tidak_memenuhi += 1
        continue

    if penghasilan <= 3000000:
        print(f"{nama}: BEASISWA PENUH")
        penuh += 1
    elif penghasilan <= 5000000:
        print(f"{nama}: BEASISWA SEBAGIAN")
        sebagian += 1
    else:
        print(f"{nama}: TIDAK MENDAPATKAN BEASISWA (penghasilan > Rp5.000.000)")
        tidak_dapat += 1

    if penuh == KUOTA_PENUH:
        print(f"\nKuota beasiswa penuh ({KUOTA_PENUH} mahasiswa) telah terpenuhi. Seleksi dihentikan.")
        break

print(f"Mahasiswa diproses        : {diproses}")
print(f"Tidak memenuhi syarat IPK : {tidak_memenuhi}")
print(f"Beasiswa penuh            : {penuh}")
print(f"Beasiswa sebagian         : {sebagian}")
print(f"Tidak mendapat beasiswa   : {tidak_dapat}")