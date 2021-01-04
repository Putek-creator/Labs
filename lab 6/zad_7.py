import random
g = 0
c = 0
n = 0
liczby = []
los = []
while n < 6:
    a = int(input("Podaj 6 szczesliwych liczb: "))
    if a > 49 or a <= 0:
        print("Liczba musi byc wieksza niz 0 i mniejsza niz 49")
    if a not in los:
         if a > 49 or a <= 0:
             continue
    los.append(a)
    n += 1

for i in range(0,6):
    while True:
        n = random.randint(1, 10)
        if n not in liczby:
            liczby.append(n)
            c += 1
            break
los.sort()
liczby.sort()
print("Twoje szczesliwe liczby to: ", los)
print("Twoje wylosowane liczby to:", liczby)
if c < 3:
    print("Nie wygrales nic sprobuj ponownie :)")
elif c == 3:
    print("Gratulacje masz 3 takie same liczby i wygrales 100 zl.")
elif c == 4:
    print("Gratulacje masz 4 takie same liczby i wygrales 10 000 zl.")
elif c == 5:
    print("Gratulacje masz 5 takie same liczby i wygrales 500 000 zl.")
elif c == 6:
    print("Gratulacje masz 6 takie same liczby i wygrales 10 000 000 zl.")