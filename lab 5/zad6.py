import random
print("Trwa generowanie Twojej losowej liczby")
a = random.randint(1,100)
n = 0
while True:
    if n == 3:
        print("Złe trafy, przegrałeś Twoja liczba to ", a)
    b = int(input("Podaj swój strzał: "))
    if a == b:
        print("Wygraleś, masz taką samą liczbę jak ta wygenerowana. ")
        break
    if b >= a:
        print("Twoja podana liczba jest większa niz wygenerowana. ")
    if a >= b:
        print("Twoja podana liczba jest mniejsza niz wygenerowana. ")
    n +=1
