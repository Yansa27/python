while True:
    # program kalkulator
    print("Selamat datang di program Kalkulator")
    nilai1 = input("masukkan angka pertama : ")
    nilai1 = int(nilai1)
    nilai2 = input("masukkan angka kedua : ")
    nilai2 = int(nilai2)

    print("Silahkan pilih jenis operator")
    print(" 1. pertambahan : + ")
    print(" 2. perkalian   : * ")
    print(" 3. pengurangan : - ")
    print(" 4. pembagian   : / ")

    operator = input("masukan nomor angka operator : ")
    operator = int(operator)
    
    if operator == 1 : 
        hasil = nilai1 + nilai2
        print("anda memilih operator pertambahan")
        print(f"{nilai1} + {nilai2} = {hasil}")
    elif operator == 2 :
        hasil = nilai1 * nilai2
        print("anda memilih operator perkalian")
        print(f"{nilai1} * {nilai2} = {hasil}")
    elif operator == 3 :
        hasil = nilai1 - nilai2
        print("anda memilih operator pengurangan")
        print(f"{nilai1} - {nilai2} = {hasil}")    
    elif operator == 4 :
        hasil = nilai1 / nilai2
        print("anda memilih operator pembagian")
        print(f"{nilai1} / {nilai2} = {hasil}")
    exit = input("apakah anda ingin melakukan perhitungan lagi ketik exit untuk keluar next untuk lanjut : ")   

    if exit == "next" :
        continue
    elif exit == "exit" :
        print("terimakasih telah menggunakan program kami..")
        break 