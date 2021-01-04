import random
tab = []
for x in range(10):
    b = random.randint(0,59)
    tab.append(b)
print(tab)
tab.append(4)
tab.insert(4,6)
tab.append(8)

print(tab)