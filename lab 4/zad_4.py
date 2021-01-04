a = 0
b = 0
n = 0
while True:
    a = input("Podaj liczbę:")
    n += 1
    if 0 == a or a == ["NULL"]:
        break
    else:
        b = int(a) + b
        print("Średnia to :", b / n)