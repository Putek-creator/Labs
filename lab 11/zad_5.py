a = int(input("Na jakiej wyskokości lecimy?[m] "))
if a/1000 > 5:
    print("Na tej wysokości jestes juz bezpieczny")
else:
    print(a/1000, "km to za nisko!")