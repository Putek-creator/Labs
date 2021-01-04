import math
i = 0
b = 0 # suma
c = 0 # ostatnia wpisana liczba
a = 0 # roznica miedzy 2 liczbami
while True:
    i = int(input("Podaj liczbę: "))
    b = b + i #liczenie sumy
    a = c - i
    if math.fabs(a) <= 5:
        print("Wartosc bezwzgledna miedzy ostatnimi liczbami jest mniejsza niz 5, suma dodawania to :", b)
        break
    c = i
    a = c - i