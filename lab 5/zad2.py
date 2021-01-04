import statistics
a = int(input("Podaj dolną granicę: "))
b = int(input("Podaj górną granicę: "))
liczby = []
i = 0
for b in range(a,b):
    if a == 0 or b == 0:
        print("Podałeś zły zakres")
        break
    print(b)
    liczby.append(b)
    if i == 5:
        break
    i += 1
print("Minimum to {}, maksimum to {}." .format(liczby[0], liczby[5]))
print("Średnia to {}.".format(sum(liczby)/len(liczby), statistics.median(liczby)))