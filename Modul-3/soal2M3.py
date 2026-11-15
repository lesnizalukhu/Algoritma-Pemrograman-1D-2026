while True:
    try:
        n = int(input("Masukkan tinggi setengah menara (2-15): "))
    except :
        print("Input tidak valid, masukkan angka bulat.")
        continue

    if 2 <= n <= 15:
        break
    print("Di luar rentang, masukkan angka 2 sampai 15.")

for baris in range(1, 2 * n):
    if baris <= n:
        i = baris
    else:
        i = 2 * n - baris

    angka = []
    for k in range(1, i + 1):
        angka.append(str(k % 10))
    for k in range(i - 1, 0, -1):
        angka.append(str(k % 10))

    print(" " * (2 * (n - i)) + " ".join(angka))