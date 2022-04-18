xy = []
def bubblesort():
    num = list(input("Podaj liczby do posortowania: "))
    for i in num:
        xy.append(int(i))

    while sortowanie(xy) is False:
        x = 0
        while x < len(xy)-1:
            a = xy[x]
            b = xy[x+1]
            if a > b:
                xy[x] = b
                xy[x+1] = a
            print(xy)

            x += 1

def sortowanie(lista):
    licznik = 1
    x = 0
    while x < len(lista)-1:
        if lista[x] <= lista[x+1]:
            licznik += 1
        x += 1
    if licznik == len(lista):
        print("posortowane")
        return True
    else:
        return False

bubblesort()
