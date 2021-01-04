sciana1 = 2 * 3 * 2.5
sciana2 = 2 * 5 * 2.5
wsciany = sciana1 + sciana2
sufit = 3 * 5
drzwi = 0.8 * 2.06
okno = 1.7 * 1.43
print("Powierzchnia ścian: ", wsciany,"m^2" )
print("Powierzchnia sufitu: ", sufit,"m^2")
print("Powierzchnia całkowita bez okien i drzwi :", wsciany + sufit)
x = int(input("Ile pokój ma mieć okien ?"))
scianyokno = wsciany - okno * x
print("Powierzchnia ścian z",x,"oknem/mi wynosi: ", scianyokno,"m^2")
print("Powierzchnia ścian z drzwiami wynosi: ", wsciany - drzwi, "m^2")
print("Całkowita powierzchnia z drzwiami i ścianami wynosi", scianyokno - drzwi + sufit, "m^2")