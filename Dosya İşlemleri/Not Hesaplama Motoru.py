while True:
    print("Üniversite Not Hesaplama Motoruna Hoşgeldiziniz...")
    print("""Lütfen aşağıdaki işlemlere göre numaraları tuşlayınız...
    1.Öğrenci Not Giris.
    2.Geçen ve Kalanları Kaydet.
    3.Geçen ve Kalanları Oku.
    4.Kayıtları Sıfırla.
    5.Çıkış.""")
    kullGiris = input("...")
    if kullGiris == "1":
        while True:
            vizeOran = int(
                input("Lütfen vizenin not ağırlık oranını yüzde cinsinden giriniz..."))
            finalOran = int(
                input("Lütfen final not ağırlık oranını yüzde cinsinden giriniz..."))
            degisken = True
            while True:
                kullGiris1 = input(
                    "Öğrenci girişi yapmak için herhangi bir tuşa,çıkmak için q'yu tuşlayınız...")
                if kullGiris1 == "q" or kullGiris1 == "Q":
                    degisken = False
                    break
                else:
                    ogrenciAd = input("Öğrencinin Adı: ")
                    vizeNot = int(input("Öğrencinin vize notu: "))
                    finalNot = int(input("Öğrencinin final notu: "))
                    note = vizeNot * (vizeOran / 100) + \
                        finalNot * (finalOran / 100)
                    if note >= 90:
                        harf = "AA"
                    elif note >= 85:
                        harf = "BA"
                    elif note >= 80:
                        harf = "BB"
                    elif note >= 75:
                        harf = "CB"
                    elif note >= 70:
                        harf = "CC"
                    elif note >= 65:
                        harf = "DC"
                    elif note >= 60:
                        harf = "DD"
                    else:
                        harf = "FF"
                    with open("ÖğrenciNot.txt", "a", encoding="utf-8") as file:
                        file.write(ogrenciAd+"->"+harf+"\n")

            if degisken == False:
                break
    elif kullGiris == "2":
        with open("ÖğrenciNot.txt", "r+", encoding="utf-8") as file:
            for i in file:
                liste = i.split("->")
                notem = liste[1]
                ad = liste[0]
                if notem == "FF\n":
                    with open("Kalanlar.txt", "a", encoding="utf-8") as file:
                        file.write(ad+"\n")
                else:
                    with open("Geçenler.txt", "a", encoding="utf-8") as file:
                        file.write(ad+"\n")
    if kullGiris == "3":
        while True:
            try:
                with open("Geçenler.txt", "r+", encoding="utf-8") as file:
                    print("*******Geçenler*******")
                    print(file.read())
                with open("Kalanlar.txt", "r+", encoding="utf-8") as file:
                    print("*******Kalanlar*******")
                    print(file.read())
            except:
                print("Dosya Bulunamadı...")
                break
    if kullGiris == "4":
        file = open("ÖğrenciNot.txt", "w")
        file1 = open("Kalanlar.txt", "w")
        file2 = open("Geçenler.txt", "w")
    if kullGiris == "5":
        break
    else:
        continue
