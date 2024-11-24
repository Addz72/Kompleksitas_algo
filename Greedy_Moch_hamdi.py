def penukaran_koin(jumlah):
    koin = [15, 10, 5, 3, 2]
    solusi = []
    
    for nilai_koin in koin:
        while jumlah >= nilai_koin:
            solusi.append(nilai_koin)
            jumlah -= nilai_koin
    
    return solusi

jumlah_koin = 12
hasil_penukaran = penukaran_koin(jumlah_koin)
print(f"Jumlah uang: {jumlah_koin}")
print(f"Solusi penukaran koin: {hasil_penukaran} ")