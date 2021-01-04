i = 333
b = 0
p = 1.08
miesiac = 0
while True:
    b += 1
    miesiac = (miesiac + i) * p
    if b == 12:
        print("Zgromadzona kwota:", float(miesiac))
        break