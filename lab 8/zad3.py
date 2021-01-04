import webbrowser
baza = {'admin':'admin', 'aaa':'aaa','bbb':'bbb','ccc':'ccc','ddd':'ddd','eee':'eee'}
login = input("Podaj login: ")
haslo = input("Podaj hasło: ")
if login in baza.keys() and haslo == baza[login]:
    webbrowser.open('http://google.com')
    print("Jestes adminem")
else:
    webbrowser.open('http://onet.pl')
    print("Nie jestes adminem")