#Problem 1

x = int(input("Lütfen ilk sayıyı giriniz...: "))
y = int(input("Lütfen ikinci sayıyı giriniz...: "))
z = int(input("Lütfen Üçüncü sayıyı giriniz...: "))

print("{} x {} x {} = {}".format(x,y,z,x*y*z))

#Problem 2

print("Hoşgeldiniz!!!")
boy = int(input("Lütfen boyunuzu cm cinsinden giriniz...: "))
kilo = int(input("Lütfen kilonuzu kg cinsinden giriniz...: "))
vki = (kilo / ((boy**2)*0.01))*100
print("Vücut Kitle Endeksiniz : ",vki)


#Problem 3 

print("Yakıt Tutarı Hesaplama Motoruna Hoşgeldiniz...")
kbyt = float(input("Lütfen aracınızın kilometre başı ne kadar yaktığını TL cinsinden giriniz : "))
yol = float(input("Lütfen gidilen yolu km cinsinden giriniz: "))

print("Yakıt masrafınız : {} TL ".format(kbyt*yol))

#Problem 4

print("Hoşgeldiniz...")
isim = input("Lütfen adınızı giriniz... : ")
numara = int(input("Lütfen numaranızı giriniz... : "))

print("Ad Soyad : {}\nNumara : {} ".format(isim,numara))



#Problem 5

x = int(input("Lütfen birinci sayıyı giriniz... : "))
y = int(input("Lütfen ikinci sayıyı giriniz... : "))
print("Birinci sayi : {}\tİkinci Sayi : {}".format(x,y))
x,y=y,x
print("Birinci sayi : {}\tİkinci Sayi : {}".format(x,y))


#Problem 6

print("Lütfen hipotenüsü bulmak için iki kenarın değerlerini giriniz...")
birinciKenar=int(input("Birinci kenar: "))
ikinciKenar = int(input("İkinci kenar: "))
print("Hipotenüs : ",(birinciKenar**2+ikinciKenar**2)**0.5)