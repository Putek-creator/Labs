from pytemp import pytemp

def MAINMENU():
    choice_valid = ['1', '2', '3', '4', '5', '6']
    print("===============================================")
    print("       Jakie dane chcesz przekonwertować?      ")
    print("===============================================")
    print("|                                             |")
    print("|           1.Celsjusze->Fahrenheit           |")
    print("|           2.Kelwin->Fahrenheit              |")
    print("|           3.Fahrenheit->Kelwin              |")
    print("|           4.Kelwin->Celsjusz                |")
    print("|           5.Celsjuz->Kelwin                 |")
    print("|           6.Koniec już wszystko wiem.       |")
    print("|                                             |")
    print("===============================================")
    while True:
        choice = input("Wybierz działanie: ")
        if choice in choice_valid:
            if choice == '1':
                CELFAH()
            elif choice == '2':
                KELFAH()
            elif choice == '3':
                FAHKEL()
            elif choice == '4':
                KELCEL()
            elif choice == '5':
                CELKEL()
            elif choice == '6':
                print("Zapraszamy ponownie.")
                quit()

def CELFAH():
    temp = int(input(("Podaj temperaturę w C: ")))
    f = pytemp(temp, 'c', 'f')
    print("Temp w F =", f)
    if f >= 212:
        print("woda wrze")
    elif f <= 32:
        print("woda zamarza")
def KELFAH():
#Kelvin -> Fahrenheit
    temp = int(input("Podaj temperature w Kelwinach:"))
    f = pytemp(temp,'k', 'f')
    print("Temp w F =", f)
def FAHKEL():
#Fahrenheit -> Kelvin
    temp = int(input("Podaj temperature w Fahrenheit:"))
    k = pytemp(temp,'f','k')
    print("Temp w Kewinach:", k)
def CELKEL():
#Celcius -> Kelvin
    temp = int(input("Podaj temperature w Celcjuszach:"))
    c = pytemp(temp,'k', 'c')
    print("Temp w Kelwinach: ",c )
def KELCEL():
#Kelvin -> Celcius
    temp = int(input("Podaj temperature w Kelwinach:"))
    k1 = pytemp(temp,'c','k')
    print("Temp w celcujszach: ", k1)
MAINMENU()
