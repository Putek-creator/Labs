def GB():
    b = 0
    x = int(input("Podaj wielkość dyku w GB: "))
    b = x
    x = x * 1000 * 1000 * 1000
    x = x / 1024 / 1024 / 1024
    print("Realna wielkość dyku to: ",round(x,2),'GB')
    print("Zostales oszukany na ",round(b - x,2),'GB')
def MB():
    b = 0
    x = int(input("Podaj wielkość dysku w MB:"))
    b = x
    x = x * 1000 * 1000
    x = x / 1024 / 1024
    print("Realna wielkość dyku to: ", round(x, 2),'MB')
    print("Zostales oszukany na ", round(b - x, 2), 'MB')
def main_menu():
    choice_valid = ['1', '2', '3']

    print("===================================================")
    print("| Witaj w kalkulatorze realnej pojemnosci dyskow !|")
    print("===================================================")
    print("|              Wybierz opcję:                     |")
    print("|                                                 |")
    print("|1.Oblicz wielkosc dysku dla warotsci GB          |")
    print("|2.Oblicz wielkosc dysku dla wartosci MB          |")
    print("|3.Wyjscie                                        |")
    print("===================================================")
    choice = int(input("Co chcesz dzisiaj zrobić ?"))
    if choice == 1:
        GB()
    elif choice == 2:
        MB()
    elif choice == 3:
        quit()
main_menu()