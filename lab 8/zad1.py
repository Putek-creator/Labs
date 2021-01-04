import operator
menu = {"rosol":6.90,"pomidorowa":7.90,"ogorkowa":8.90,"ramen":14.90,"kurczak z ryzem":19.99,"spaghetti":13.99,"nalesniki":10.00,"cola":2.00,"spite":2.50,"fanta":3.50,"mirinda":3.00}
for wartosc in menu.values():
    print(wartosc)
for klucz in menu.keys():
    print(klucz)
for klucz,wartosc in menu.items():
    print(klucz, wartosc)
sorted_menu= sorted(menu.items(), key=operator.itemgetter(1))
print(sorted_menu)
del sorted_menu[0]
del sorted_menu[-1]
print(sorted_menu)
a = input("Podaj nazwe dania: ")
b = input("Podaj cene dania: ")
menu[a] = b
print(menu)
