n = int(input("Podaj liczbę a ja wypisze Ci wszystkie jej dzielniki: "))
i = 1
dziel = []
while i <=n:
    if (n % i ==0):
        dziel.append(i),
    i = i + 1
print("Dzielniki liczby", (n), "to: ", dziel)