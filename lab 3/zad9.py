import random
print("1 - LOTTO")
print("2 - Multi Muti")
print("3 - Mini LOTTO")
a = int(input("Wybierz rodzaj losowania :"))
liczby = []
n = 0
if a == 1:
    for i in range(0,6):
        while True:
            n = random.randint(1, 50)
            if n not in liczby:
                liczby.append(n)
                break
    print("Twoje liczby to:", liczby)
if a == 2:
    for i in range(0, 20):
        while True:
            n = random.randint(1, 80)
            if n not in liczby:
                liczby.append(n)
                break
    print("Twoje liczby to:", liczby)
if a == 3:
    for i in range(0,5):
        while True:
            n = random.randint(1, 42)
            if n not in liczby:
                liczby.append(n)
                break
    print("Twoje liczby to:", liczby)
print("Dziękujemy za grę :) i twoje pieniadze")