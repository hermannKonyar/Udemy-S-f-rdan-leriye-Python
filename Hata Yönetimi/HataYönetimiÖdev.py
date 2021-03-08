#Problem 1

liste = ["345", "asdasd", "432a", "14", "kemal"]

for i in liste:
      try:
        print(int(i))
      except ValueError:
        continue

#Problem 2

def ciftMiTekMi(sayi):
      if sayi%2==0:
            return sayi
      else:
            raise ValueError("Tek sayıdır")


liste = [34, 2, 1, 3, 33, 100, 61, 1800]
for i in liste:
      try:
        print(ciftMiTekMi(i))
      except ValueError:
        pass
