def hitung_ips(jumlah_matkul):
    total_sks = jumlah_matkul * 3
    bobot = 0

    for i in range(jumlah_matkul):
        nilai = input(f"    Nilai matkuk ke-{i + 1} (A, B, C, atau D): ").upper()

        if nilai == 'A':
            bobot += 4 * 3  
        elif nilai == 'B':
            bobot += 3 * 3  
        elif nilai == 'C':
            bobot += 2 * 3  
        elif nilai == 'D':
            bobot += 1 * 3 
        else:
            print("Input nilai tidak valid. Harap masukkan A, B, C, atau D.")
            return None

    ips = bobot / total_sks
    return ips

jumlah_matkul = int(input("Masukkan jumlah matkul anda: "))

hasil_ips = hitung_ips(jumlah_matkul)

if hasil_ips is not None:
    print(f"Nlai IPS anda semester ini: {hasil_ips:.2f}")
