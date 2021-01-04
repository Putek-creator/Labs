a = int(input("Podaj pierwsza liczbę: "))
b = int(input("Podaj druga liczbe:"))
print("Suma liczb:", a + b)
print("Roznica liczb:", a - b)
print("Roznica liczb:", a * b)
if b == 0 or a == 0:
    print("Nie dzielimy przez zero :)")
else:
    print("Iloraz liczb:", a % b)