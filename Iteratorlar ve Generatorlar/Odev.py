# Program 1

class Kareler():
    def __init__(self, max):
        self.max = max
        self.sayi = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= self.max:
            sonuc = self.sayi ** 2
            self.sayi += 1
            return sonuc
        else:
            self.sayi = 1
            raise StopIteration


kareler = Kareler(5)
for i in kareler:
    print(i)

# Program 2


def asal_mı(sayı):
    i = 2

    while i < sayı:
        if (sayı % i == 0):
            return False
        i += 1
    return True


def asal_generator():
    i = 2
    while True:
        if (asal_mı(i)):
            yield i
        i += 1


for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)
