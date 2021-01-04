import random
c = 0
w = 0
n = int(input("Podaj dolny zakres liczb: "))
b = int(input("Podaj gorny zakres liczb: "))
a = int(input("Podaj ile liczb chcesz wygenerowac: "))
tab = []
mytab = []
while a > w:
    c = random.randint(n, b)
    tab.append(c)
    w += 1
tab = list(dict.fromkeys(tab))
print("Oto twoja wygenerowana lista", tab)
tab = list(dict.fromkeys(tab))
print("To jest twoja lista bez duplikatow", tab)
print("Twoja lista liczy ", len(tab), " liczb")