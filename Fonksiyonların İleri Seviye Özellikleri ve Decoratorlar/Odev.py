def mukemmelSayilar(func):

    def wrapper(sayilar):
        toplam = 0
        for i in sayilar:
            toplam = 0
            for j in range(1, i):
                if i % j == 0:
                    toplam += j
            if toplam == i:
                print("Mükemmel Sayı: ", i)
        func(sayilar)
    return wrapper


@mukemmelSayilar
def hello(sayilar):
    for i in sayilar:
        bool = False
        for j in range(2, i):
            if i % j == 0:
                bool = True
                break
        if bool == False:
            print(i)


hello(range(1, 1001))
