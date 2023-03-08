from math import tan, radians

while True:
    jarakawal = input("Masukkan jarak awal (dalam meter): ")
    if jarakawal.lower() == "stop" or jarakawal.lower() == "berhenti":
        print("Program dihentikan")
        break
    else:
        jarakawal = float(jarakawal)
        sudutmenit5 = float(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): "))
        sudutmenit6 = float(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): "))
        tinggiawal = jarakawal * tan(radians(sudutmenit5))
        jarakakhir = jarakawal * (tan(radians(sudutmenit6)) - tan(radians(sudutmenit5)))
        selisihketinggian = jarakakhir * tan(radians(sudutmenit6))
  
        print("Ketinggian drone pada menit ke-5 adalah {:.2f} meter".format(tinggiawal))
        print("Selisih ketinggian drone saat menit ke-5 dan ke-6 adalah {:.2f} meter".format(selisihketinggian))
