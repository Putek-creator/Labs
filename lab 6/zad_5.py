import random
g = 0
c = 0
w = 0
n = int(input("Podaj dolny zakres liczb: "))
b = int(input("Podaj gorny zakres liczb: "))
a = int(input("Podaj ile liczb chcesz wygenerowac: "))
tab = []
mytab = []
duplikaty = []
while a > w:
    c = random.randint(n, b)
    tab.append(c)
    w += 1
tab.sort()
print("Oto twoja wygenerowana lista",tab)
print("Trzecia liczba od konca",tab[-3])
c = int(input("Ktora liczbe od konca chcesz usunac"))
tab.pop(-c)
print("Oto lista bez", c,"elementu od tylu",tab)
w = 0
while a > w:
    g = random.randint(n, b)
    mytab.append(g)
    w += 1
mytab = mytab + tab
print("Twoja lista liczy ", len(mytab), " liczb")
