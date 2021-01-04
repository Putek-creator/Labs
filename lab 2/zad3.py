a = int(input("podaj pierwsza liczbe"))
b = int(input("podaj druga liczbe"))
c = int(input("podaj trzecia liczbe"))
if a > b and a > c:
    print("Pierwsza liczba jest najwieksza")
elif b > a and b > c:
    print("Druga liczba jest najwieksza")
elif c > a and c > b:
    print("Trzecia liczba jest najwieksza")
else:
    print("nie ma najwiekszej liczby")
if a == b and a == c:
    print("Wszystkie liczby sa takie same")
elif a == b:
    print("Pierwsza i druga liczba jest taka sama")
elif a == c:
    print("Pierwsza i druga liczba jest taka sama")
elif b == c:
    print("Druga i trzecia liczba jest taka sama")