kesempatan = 0
secret_number = 9
limit = 3
countLimit = 3

while kesempatan < limit: 
    number = input("Masukan angka (1-9) ")
    number = int(number)
    if number == secret_number :
        print("Selamat anda benar")
        break
    else:  
        countLimit -= 1      
        print("Mohon maaf jawaban anda kurang tepat")
        print("Anda bisa mencoba " + str(countLimit) + " lagi")
        if countLimit == 0 :
            print("sisa percobaan anda telah habis")
            print("Anda kalah")
    kesempatan += 1