class Pojazd:
    def __init__(self, nr_tablica, marka, model):
        self.nr_tablica = nr_tablica
        self.marka = marka
        self.model = model

    def pokaz_dowod(self):
        print("Nr tablicy rejestracyjnej to {} ".format(self.nr_tablica))

    def __del__(self):
        print("{} własnie mial wypadek i sie rozbil".format(self.marka))


class Samochod(Pojazd):
    def __init__(self, nr_tablica, marka, model, rozm_felg):
       super().__init__(nr_tablica, marka, model)
       self.rozm_felg = rozm_felg

    def tuning(self):
        print("Samochod marki {} model {} właśnie zmienił felgi na {}".format(self.marka, self.model, self.rozm_felg))


class Motocykl(Pojazd):
    def __init__(self, nr_tablica, marka, model, waga):
        super().__init__(nr_tablica, marka, model)
        self.waga = waga

    def wazenie(self):
        print("Motocykl marki {} waży {} i jest idealny dla kobiet".format(self.marka, self.waga))

bmw = Samochod("DW 5OM237", "BAWARA","SERIA 5", "19 cali")
yama = Motocykl("WRO 9DG17", "yamaha", "speed", 100)

bmw.tuning()
yama.wazenie()