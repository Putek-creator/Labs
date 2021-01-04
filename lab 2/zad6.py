liczby = []
n = 0
while n <= 3:
    x = int(input("Podaj liczbę: "))
    liczby.append(x)
    n += 1
liczby.sort()
print(liczby[-1], liczby[-2] )