a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
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
def pierw(a,b):
    a = a*a
    b = b*b
    return a and b

print(suma(a,b))
print(minus(a,b))
print(mnoz(a,b))
print(dziel(a,b))
print(pierw(a,b))