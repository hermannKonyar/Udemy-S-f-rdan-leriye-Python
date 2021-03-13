# Problem 1

s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
sozluk = dict()
for i in s:
    if i in sozluk:
        sozluk[i] += 1
    else:
        sozluk[i] = 1
for i, j in sozluk.items():
    print(i, ":", j)

# Problem 2

sozcuk = ""
with open("dd.txt", "r+", encoding="utf-8") as file:
    for i in file:
        sozcuk += i[0]
print(sozcuk)

# Problem 3

with open("dd.txt", "r", encoding="utf-8") as file:
    for i in file:
        i = i[:-1]
        if i.endswith(".com") and i.find("@") != -1:
            print(i+"\n")

# Problem 4

isim = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
soyIsim = ["Yılmaz", "Öztürk", "Dağdeviren",
           "Atatürk", "Dikmen", "Kaya", "Polat"]
liste = list(zip(isim, soyIsim))
liste.sort()
for i, j in liste:
    print(i, j)
