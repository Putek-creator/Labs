a = 0
b = 0
while True:
    a = int(input("Podaj liczbę"))
    b = a + b
    if b >= 100:
        print("Suma liczb jest większa niz 100", b)
        break
    if b % 66 == 0:
        print("Średnia wynosi 66")