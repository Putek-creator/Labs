import random #wpowadzialem mozliwosc wybrania przedzialu i ilosci elementow w lisice
c = 0
w = 0
n = int(input("Podaj dolny zakres liczb: "))
b = int(input("Podaj gorny zakres liczb: "))
a = int(input("Podaj ile liczb chcesz wygenerowac: "))
tab = []
while a > w:
    c = random.randint(n, b)
    tab.append(c)
    w += 1
print(tab)
tab.sort()
print(tab)
tab.sort(reverse=1)
print(tab)