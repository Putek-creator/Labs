a = float(input("Podaj ilość alkoholu w wydychanym powietrzu(mg/L):"))
b = a * 2.1
print("Wynik w promilach", b, "%o")

if((b == 0.2) or (b < 0.2)):
    print("Jesteś trzeźwy mozesz jechać:")
else:
    print("Jesteś pijany i nie mozesz jechac")