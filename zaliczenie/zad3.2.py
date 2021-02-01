import random
def get_tof_statements():

    statements = []
    statements.append(["Jak coś nie działa to resetujemy?", "T"])
    statements.append(["Czy python jest trudny?", "N"])
    statements.append(["Czy 64GB ramu to dużo?", "T"])
    statements.append(["Czy każdy programista kocha koty?", "T"])
    statements.append(["Czy kaażdy programista zarabia conajmniej 15 tys zl?", "T"])
    statements.append(["Czy dysk o pojemnosci 5 TB jest wystarczający?", "T"])
    statements.append(["Czy komputer może działać bez procesora?", "N"])
    statements.append(["Czy każdy informatk naprawi babci telefon?", "T"])
    statements.append(["Czy programista przeżyje bez kawy?","N"])
    statements.append(["Czy memy z kotami poprawią informatykowi chumor ?", "T"])

    return statements



def play_tof_quiz():
    tof_statements = get_tof_statements()
    random.shuffle(tof_statements)
    valid_options = ['T','N']
    score = 0
    for s in tof_statements:
        print("Tak czy Nie: " +s[0])
        while True:
            guess = input("Odpowiedz T lub N: ")
            if guess in valid_options:
                if guess == s[1]:
                    print("Dobra odpowiedź")
                    score +=  1
                    break
                else:
                    print("Zła odpowiedź :(")
                    break
            else:
                continue
    print("Uzyskałeś ",score,"punktów na ", len(tof_statements)," możliwych")
    proc = score / len(tof_statements)
    if proc <= 0.3:
        print("Uzyskałeś ocenę niedostateczną.")
        main_menu()
    elif proc > 0.31 and proc < 0.45:
        print("Uzyskałeś ocenę dopuszczajaca.")
    elif proc > 0.45 and proc < 0.6:
        print("Uzyskales ocene dostateczna.")
    elif proc > 0.61 and proc < 0.75:
        print("Uzyskales ocene dobra.")
    elif proc > 0.76 and proc < 0.9:
        print("Uzyskales ocene bardzo dobra.")
    elif proc > 0.9:
        print("Uzyskales ocene celujaca.")
def main_menu():
    choice_valid = ['1', '2']

    print("======================")
    print("| Witaj w Quizie !   |")
    print("======================")
    print("|   Wybierz opcję:   |")
    print("|                    |")
    print("|1.Zagraj w Quiz     |")
    print("|2.Wyjście           |")
    print("|                    |")
    print("======================")
    while True:
        choice = input("Wybierz 1 lub 2: ")
        if choice in choice_valid:
            if choice == '1':
                print("Rozpoczynamy Quiz !")
                play_tof_quiz()
            elif choice == '2':
                print("Dzięki za grę!")
                quit()
        else:
            continue
main_menu()