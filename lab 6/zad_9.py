a = int(input("Podaj ilosc elementow w Twoim ciagu: "))
b = 1
e = 0
tab = []
while a >= b:
    c = int(input("Podaj liczbe: "))
    tab.append(c)
    b += 1
print(tab)
tab.sort()
d = tab[-1]
print("Najwiekszy element w ciagu to: ",d)
for d in tab:
    e += 1
print("Wystepuje", e,"razy")