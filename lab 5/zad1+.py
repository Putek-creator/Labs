import random
n = random.randint(1,10)
sum = 0
i = n
int_count = 0
float_count = 0

while i > 0:
    inp = float(input("Podaj liczbę: "))
    if inp.is_integer():
        int_count += 1
    else:
        float_count += 1
    if inp < 0:
        continue
    sum = sum + inp
    i -= 1

print("Średnia arytmetyczna twoich liczb to {}.".format(sum/n))
print("Wystąpiło {} floatów i {} intów".format(float_count, int_count))