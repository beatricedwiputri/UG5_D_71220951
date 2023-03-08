def ganti_kata(kalimat, cari, ganti):
    kata = kalimat.split()
    for i in range(len(kata)):
        if kata[i] == cari:
            kata[i] = ganti
        else:
            pass

    kalimatbaru = ' '.join(kata)
    return kalimatbaru


kalimat = input("Masukkan kalimat : ")
cari = input("Kata yang dicari : ")
ganti = input("Diganti menjadi : ")

print("Kalimat baru :", ganti_kata(kalimat, cari, ganti))

