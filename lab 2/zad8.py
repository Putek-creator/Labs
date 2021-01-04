a = int(input("Podaj dlugosc 1 boku:"))
b = int(input("Podaj dlugosc 2 boku:"))
c = int(input("Podaj dlugosc 3 boku:"))
if a*2+b*2 == c*2 or a*2+c*2 == b*2 or c*2+b*2 == a*2:
    print("Trojkat jest prostokatny")
else:
    print("Trojkat nie jest prostokatny")