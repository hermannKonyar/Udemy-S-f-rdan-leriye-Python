from functools import reduce
# Problem 1

print(list(map(lambda x: x[0] * x[1], [(3, 4), (10, 3), (5, 6), (1, 9)])))

# Problem 2


def dikUcgenMi(x):
    if x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[1] + x[2] > x[0]:
        return True
    return False


liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]
print(list(filter(dikUcgenMi, liste)))

# Problem 3

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtre = list(filter(lambda x: x % 2 == 0, liste))
print(reduce(lambda x, y: x + y, filtre))

#Problem 4

isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
soyIsimler = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

listem = list(zip(isimler, soyIsimler))
for i in listem:
    print(i[0],i[1])
