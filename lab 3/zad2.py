a = int(input("podaj zakres liczb "))
for i in range(a,0,-1):
    if i % 6 == 0 and i % 9 == 0:
        print(i)
