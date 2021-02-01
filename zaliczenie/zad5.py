#KURSY POBRANE ZE STRONY GOOGLE 28.01.2020
def THBUSD():
    print('1. THB->USD, 2. USD->THB')
    choice_valid = ['1','2']
    while True:
        choice = input("Wybierz 1 lub 2: ")
        if choice in choice_valid:
            if choice == '1':
                x = int(input("Podaj ilość BTH: "))
                b = x * 0.33
                print(x,'BTH to', round(b, 2), 'USD')
                break
            elif choice == '2':
                x = int(input("Podaj ilość USD: "))
                b = x * 30
                print(x, 'USD to',round(b, 2), 'BTH')
                break
        else:
            continue

def BTCUSD():
    print('1. BTC->USD, 2. USD->BTC')
    choice_valid = ['1','2']
    while True:
        choice = input("Wybierz 1 lub 2: ")
        if choice in choice_valid:
            if choice == '1':
                x = int(input("Podaj ilość BTC: "))
                b = x * 32250.5
                print(x,'BTC to', round(b, 2), 'USD')
                break
            elif choice == '2':
                x = int(input("Podaj ilość USD: "))
                b = x * 0.000031
                print(x, 'USD to', b , 'BTC')
                break
        else:
            continue

def BTNUSD():
    print('1. BTN->USD, 2. USD->BTN')
    choice_valid = ['1','2']
    while True:
        choice = input("Wybierz 1 lub 2: ")
        if choice in choice_valid:
            if choice == '1':
                x = int(input("Podaj ilość BTN: "))
                b = x * 0.014
                print(x,'BTN to', round(b, 2), 'USD')
                break
            elif choice == '2':
                x = int(input("Podaj ilość USD: "))
                b = x * 73.05
                print(x, 'USD to',round(b, 2), 'BTN')
                break
        else:
            continue

def MROUSD():
    print('1. MRO->USD, 2. USD->MRO')
    choice_valid = ['1','2']
    while True:
        choice = input("Wybierz 1 lub 2: ")
        if choice in choice_valid:
            if choice == '1':
                x = int(input("Podaj ilość MRO: "))
                b = x * 0.028
                print(x,'MRO to', round(b, 2), 'USD')
            elif choice == '2':
                x = int(input("Podaj ilość USD: "))
                b = x * 36.06
                print(x, 'USD to',round(b, 2), 'MRO')
        else:
            continue

def ETHUSD():
    print('1. ETH->USD, 2. USD->ETH')
    choice_valid = ['1','2']
    while True:
        choice = input("Wybierz 1 lub 2: ")
        if choice in choice_valid:
            if choice == '1':
                x = int(input("Podaj ilość ETH: "))
                b = x * 1335.2
                print(x,'ETH to', round(b, 2), 'USD')
                break
            elif choice == '2':
                x = int(input("Podaj ilość USD: "))
                b = x * 0.00074
                print(x, 'USD to',  b, 'ETH')
        else:
            continue

def main_menu():
    choice_valid = ['1', '2', '3','4','5','6']

    print("====================================================")
    print("|            Witaj w wirtualnym kantorze !         |")
    print("====================================================")
    print("| Wybierz parę walut na ktorych chcesz operowac:   |")
    print("|                                                  |")
    print("|                 1.TBH USD                        |")
    print("|                 2.BTC USD                        |")
    print("|                 3.BTN USD                        |")
    print("|                 4.MRO USD                        |")
    print("|                 5.ETH USD                        |")
    print("|                 6.Wyjscie                        |")
    print("====================================================")
    while True:
        choice = input("Wybierz nr operacji: ")
        if choice in choice_valid:
            if choice == '1':
                THBUSD()
            elif choice == '2':
                BTCUSD()
            elif choice == '3':
                BTNUSD()
            elif choice == '4':
                MROUSD()
            elif choice == '5':
                ETHUSD()
            elif choice == '6':
                print("Dziękuje i zapraszam ponownie")
                quit()
        else:
            continue
main_menu()