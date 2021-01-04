import random
lista = []
a = 0
b = 0
for i in range(0,100):
    num = random.randint(0, 10)
    lista.append(num)
    if num % 2 == 0:
        a += 1
    else:
        b += 1
tup = tuple(lista)
print(tup)
print("Liczba 1 wystapila:", tup.count(1),"Liczba 0 wystapila:", tup.count(0),"Liczba 2 wystapila:", tup.count(2))
print(" Ilość liczby parzyste:", a, "Ilość liczby nieparzyste ", b)