def pracodawcabrutto():
    x = int(input("Podaj kwote brutto: "))
    emeryt = 0.0976 * x
    wyp = 0.0167 * x
    rent = 0.065 * x
    fun = 0.0245 * x
    fgsp = 0.008 * x
    print("Koszt dla płacy brutto", x,", wynosi pracodawcę:",x + emeryt + wyp + rent + fun + fgsp)

def pracodawcanetto():
    x = int(input("Podaj kwote netto: "))
    b = x
    x = 1.3534 * x #wziete z poprzedniego zadania :(
    emeryt = 0.0976 * x
    wyp = 0.0167 * x
    rent = 0.065 * x
    fun = 0.0245 * x
    fgsp = 0.008 * x
    print("Koszt dla płacy netto", b,"wynosi pracodawcę: ",x + emeryt + wyp + rent + fun + fgsp)

def main_menu():
    choice_valid = ['1', '2','3']

    print("================================")
    print("|        Wybierz opcję:        |")
    print("|                              |")
    print("|1.Policz koszt dla brutto     |")
    print("|2.Policz koszt dla netto      |")
    print("|3.Wyjście                     |")
    print("|                              |")
    print("================================")
    while True:
        choice = input("Wybierz co chcesz robic: ")
        if choice in choice_valid:
            if choice == '1':
                pracodawcabrutto()
            elif choice == '2':
                pracodawcanetto()
            elif choice == '3':
                print("Dzieki za gre")
                quit()
        else:
            continue

