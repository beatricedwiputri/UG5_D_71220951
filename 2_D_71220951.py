def hitung_mobil():
    jumlahSol = 0
    jumlahSur = 0
    jumlahJog = 0
    jumlahMag = 0

    mobil = input("masukkan asal mobil (ketik \"done\" untuk keluar): ").lower()

    while mobil != "done":
        if mobil == "solo":
            jumlahSol += 1
        elif mobil == "surabaya":
            jumlahSur += 1
        elif mobil == "jogja":
            jumlahJog += 1
        elif mobil == "magelang":
            jumlahMag += 1
        else:
            pass
        
        mobil = input("Masukkan asal mobil (ketik \"done\" untuk keluar): ").lower()

    print("")
    print("Jumlah Mobil Solo        :", jumlahSol)
    print("Jumlah Mobil Surabaya    :", jumlahSur)
    print("Jumlah Mobil Jogja       :", jumlahJog)
    print("Jumlah Mobil Magelang    :", jumlahMag)

hitung_mobil()
