import random
druzyny = ['Bayern', 'Rb Salzburg','Lokomotiv','Real Madryt','Szachtar','Inter Mediolan','Porto','Liverpool','Borussia','Chelsea','Lazio','Zenit','Juventus','FC Barcelona','Dynamo Kijow','PSG','RB Lepizg','Man Utd','Krasnodar','Club Brugge']
set1 = {0}
set2 = {0}
set3 = {0}
set4 = {0}
set1.discard(0)
set2.discard(0)
set3.discard(0)
set4.discard(0)
for x in range(10): 
    while True:
        n = random.choice(druzyny)
        if n not in set1:
            set1.add(n)
            break
    while True:
        n = random.choice(druzyny)
        if n not in set2:
            set2.add(n)
            break
    while True:
        n = random.choice(druzyny)
        if n not in set3:
            set3.add(n)
            break
    while True:
        n = random.choice(druzyny)
        if n not in set4:
            set4.add(n)
            break
print(set1)
print(set2)
print(set3)
print(set4)
set12 = set1.intersection(set2)
set34 = set3.intersection(set4)
intersection_set = set12.intersection(set34)
print("Wspólny element grup: ",intersection_set)
print("Wspólny element 1 i 2 grupy:", set1.union(set2))
print("Wspólny element 3 i 4 grupy:", set3.union(set4))
print("Czy grupa 2 jest podzbiorem gr 1", set1.issuperset(set2))
print("Czy grupa 4 jest podzbiorem gr 3", set3.issuperset(set4))
print("Czy grupa 2 jest podzbiorem gr 3", set2.issubset(set3))
print("Czy grupa 4 jest podzbiorem gr 1", set4.issubset(set1))
print(len(set1))
print(len(set2))
print(len(set3))
print(len(set4))