class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def showLicznik(self):
        print(self.licznik)

    def showMianownik(self):
        print(self.mianownik)

    def add(self):
        return self.licznik + self.mianownik

    def substr(self):
        return self.licznik - self.mianownik

    def multiplication(self):
        return self.licznik * self.mianownik

    def division(self):
        return self.licznik / self.mianownik



