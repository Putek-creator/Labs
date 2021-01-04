num = int(input("Podaj liczbe: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num," to nie jest liczba pierwsza")
            print(i,"razy",num//i,"jest",num)
            break
    else:
        print(num,"jest liczba pierwsza")
else:
    print(num,"nie jest liczba pierwsza")