def suma(a,b):
     c = a + b
     return c
def minus(a,b):
     c = a - b
     return c
def mnoz(a,b):
     c = a * b
     return c
def dziel(a,b):
    if b == 0:
        print("Nie dziel przez zero")
    else:
        c = a / b
        return c
def pierw(a,):
    a = a*a
    return a
print("""
      1- Dodawanie:
      2- odejmowanie
      3- mnozenie
      4- dzielenie
      5- pierwiastek kwadratowy""")
wybor = int(input("Podaj jakie dzialanie chcesz wykonac: "))
if wybor == 1:
    a = int(input("Podaj pierwsza liczbe:"))
    b = int(input("Podaj druga liczbe:"))
    print("Suma dodawania to", suma(a,b))
elif wybor == 2:
    a = int(input("Podaj pierwsza liczbe:"))
    b = int(input("Podaj druga liczbe:"))
    print("Odejmowanie:",minus(a,b))
elif wybor == 3:
    a = int(input("Podaj pierwsza liczbe:"))
    b = int(input("Podaj druga liczbe:"))
    print("Mnożenie:",mnoz(a,b))
elif wybor == 4:
    a = int(input("Podaj pierwsza liczbe:"))
    b = int(input("Podaj druga liczbe:"))
    if b == 0:
        print("Nie dzielimy przez zero :)")
    else:
        print("Dzielenie",dziel(a,b))
elif wybor == 5:
    a = int(input("Podaj pierwsza liczbe:"))
    print(pierw(a))
elif wybor > 5 or wybor < 0:
    print("Nie wybrales zadnego dzialania")
