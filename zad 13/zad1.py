class samochod:
    def __init__(self, marka, kolor, rodzaj, cena, przebieg, naped):
        self.marka = marka
        self.kolor = kolor
        self.rodzaj = rodzaj
        self.cena = cena
        self.przebieg = przebieg
        self.naped = naped

    def jezdz_prosto(self,przyspieszenie):
        return "Samochod marki {} jedzie prosto i przyspiesza o {} km/h".format(self.marka, przyspieszenie)

    def jedz_lewo(self):
        return 'Samochod o kolorze {} skreca w lewo'.format(self.kolor)

    def jedz_prawo(self):
        return "samochod o rodzaju {} jedzie w prawo".format(self.rodzaj)

    def stop(self):
        return 'samochod o przebiegu {} zatrzymal sie'.format(self.przebieg)

    def otwarta_maska(self):
        return "samocnod o napedzie {} ma otwarta maske".format(self.naped)


ferrari = samochod('ferrari','czerwony','kabriolet', 60000, 160000, 'tyl' )
print(ferrari.jezdz_prosto(100))
