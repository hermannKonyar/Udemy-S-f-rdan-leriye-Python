import random

sayi = 0
sayi1 = int()
matris = []


for i in range(10):
    asalMi = True
    for j in range(1000):
        sayi = random.randint(2,100)
        for k in range(2,sayi):
            if sayi % k == 0 :
                asalMi = False
                break
        if asalMi == True:
            sayi1 = sayi
            break
    matris.append(sayi1)
print(matris[0:3])
print(matris[4:7])
print(matris[7:10])

    


            
            



