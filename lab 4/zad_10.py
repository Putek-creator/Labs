b = 0 # suma
c = 0 # ostatnia wpisana liczba
while True:
    i = int(input("Podaj liczbę: "))
    b = i + b
    if c == i:
        print("Podałeś dwie takie same liczby a suma dodawania to:", b)
        break
    else:
        c += i