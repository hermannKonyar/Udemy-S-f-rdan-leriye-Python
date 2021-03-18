from deneme import *

while True:
    veritabanim = Veritabani()
    veritabanim.baglanti_Olustur()
    print("""********Hoşgeldiniz*********
    Lütfen Seçim Yapınız...
    1.Şarkı Ekle.
    2.Şarkı Sil.
    3.Veritabanındaki Şarkıların Toplam Süresi.
    4.Vertitabanındaki Şarkıları Gör.
    5.Çıkış.

    """)
    secim = input("Seçiminiz: ")
    if secim == "1":
        ad = input("Şarkı Adı: ")
        sanatci = input("Sanatçı Adı: ")
        album = input("Albüm Adı: ")
        sirket = input("Şirket Adı: ")
        sure = float(input("Süre: "))
        sarki = Sarki(ad, sanatci, album, sirket, sure)
        veritabanim.sarkiEkle(sarki)
    elif secim == "2":
        ad = input("Silinecek Şarkı Adı: ")
        veritabanim.sarkiSil(ad)
    elif secim == "3":
        print("Toplam Süre:", veritabanim.sureHesapla())
    elif secim == "4":
        veritabanim.sarkilariGoster()
    elif secim == "5":
        break
    else:
        "Yanlış Tuşladınız...."
