liczby = []
for i in range(1001):
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        liczby.append(i)

liczby.sort()
print(liczby[-1])