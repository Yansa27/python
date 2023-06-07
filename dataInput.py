nama = []
umur = []
berapa_data = int(input("mau berapa data: "))
for i in range(0 , berapa_data) :
    data_nama = input("masukkan nama: ")
    data_umur = int(input("masukkan umur: "))

    nama.append(data_nama)
    umur.append(data_umur)

for i in range(0 , len(nama)) :
    indexNama = nama[i]
    indexUmur = umur[i]
    print(f" nama : {indexNama} berumur : {indexUmur}")