#Problem 1

def mukemmel_sayi(sayi):
    temp = 0
    for i in range(1,sayi):
        if sayi%i==0:
            temp+=i
    return sayi == temp
for i in range(1,1001):
    if mukemmel_sayi(i):
        print(i,"Mükemmel Sayıdır.")

#Problem 2

def obeb_bul(a,b):
    obeb = 1
    x = 1
    while x<=a and x<=b:
        if not(a%x) and not(b%x):
            obeb = x
        x+=1
    return obeb
sayi1 = int(input("Birinci sayi: "))
sayi2 = int(input("İkinci sayi: "))
print(obeb_bul(sayi1,sayi2))

#Problem 3

def okek_bul(a,b):
    okek = 1
    y = 2
    while True:
        if a % y == 0 and b % y == 0:
            okek *= y

            a //= y
            b //= y
        elif a % y == 0 and b % y != 0:
            okek *= y

            a//=y
        elif a % y != 0 and b % y == 0:
            okek *= y

            b//=y
        else:
            y+=1
        if a == 1 and b == 1:
            break
    return okek




sayi1 = int(input("Birinci sayi: "))
sayi2 = int(input("İkinci sayi: "))
print(okek_bul(sayi1,sayi2))

















