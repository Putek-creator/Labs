def netto():# skladki emerytalna 9,76 rentowa 1.5 chorobowa 2,45 zdrowontan 9
    x = int(input("Podaj wynagrodzenie brutto"))
    emerytal = 0.0976 * x #emerytalna
    rent = 0.015 * x  #rentowe 1.5
    chrob = 0.0245 * x #choronowe 2,45
    podst = x - (emerytal + rent + chrob)
    zdrow = podst * 0.09 #zdrowotne 9
    podst2 = emerytal + rent + chrob +zdrow
    kwota = x - podst2
    zus = podst * 0.0775 # zus 7,75
    zalicza = kwota * 0.17 - 43.76 - zus
    if zalicza < 0:
        zalicza = 0

    print('Kwota netto wynnosi: ',round(x - (emerytal + rent + chrob + zdrow + zalicza), 2))
    print("Skladki wynoszą:")
    print( "emerytalne :", emerytal)
    print("rentowa: ", rent)
    print("chorobowa: ",chrob)
    print("zdrowotna: ",zdrow)
    print("zus: ",zus)
    print("zaliczka na podatek: ",zalicza)

def brutto():
    x = int(input("Podaj kwotę netto: ")) #policzylem dosc prymitywnie i niezbyt dokladnie
    x = x * 1.3534                       # 100% -1912 x - 2587,76 brutto i x = 135.34% wyszlo i wrzucilem
    print(x)

def main_menu():
    choice_valid = ['1', '2','3']

    print("======================")
    print("|   Wybierz opcję:   |")
    print("|                    |")
    print("|1.Policz brutto     |")
    print("|2.Policz netto      |")
    print("|3.Wyjście           |")
    print("|                    |")
    print("======================")
    while True:
        choice = input("Wybierz co chcesz robic: ")
        if choice in choice_valid:
            if choice == '1':
                brutto()
            elif choice == '2':
                netto()
            elif choice == '3':
                print("Dzieki za gre")
                quit()
        else:
            continue
