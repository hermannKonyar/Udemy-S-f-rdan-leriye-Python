import sqlite3


class Sarki():
    def __init__(self, sarkiIsmi, sanatci, album, sirket, sure):
        self.sarkiIsmi = sarkiIsmi
        self.sanatci = sanatci
        self.album = album
        self.sirket = sirket
        self.sure = sure

    def __str__(self):
        return "Şarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nŞirket: {}\nSüre: {}".format(self.sarkiIsmi, self.sanatci, self.album, self.sirket, self.sure)


class Veritabani():
    def __init__(self):
        self.baglanti_Olustur()

    def baglanti_Olustur(self):
        self.baglanti = sqlite3.connect("Şarkı.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS ŞARKILAR(Şarkı Adı TEXT,Sanatçı TEXT,Albüm TEXT,Şirket TEXT,Süre INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyiSonlandir(self):
        self.baglanti.close()

    def sarkilariGoster(self):
        sorgu = "SELECT * FROM ŞARKILAR"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        for i in sarkilar:
            sarki = Sarki(i[0], i[1], i[2], i[3], i[4])
            print("****************")
            print(sarki)
            print("****************")

    def sarkiEkle(self, sarki):
        sorgu = "INSERT INTO ŞARKILAR VALUES(?,?,?,?,?)"
        self.cursor.execute(
            sorgu, (sarki.sarkiIsmi, sarki.sanatci, sarki.album, sarki.sirket, sarki.sure,))
        self.baglanti.commit()

    def sarkiSil(self, isim):
        sorgu = "DELETE FROM ŞARKILAR WHERE Şarkı=?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()

    def sureHesapla(self):
        sorgu = "SELECT Süre FROM ŞARKILAR"
        self.cursor.execute(sorgu)
        sureler = self.cursor.fetchall()
        self.toplam = 0

        for i in sureler:
            self.toplam += i[0]
        return self.toplam
