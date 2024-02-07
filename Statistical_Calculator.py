import pandas as pd
import time
class Statystyka:
    def __init__(self, dane):
        self.dane = dane

    def srednia_arytmetyczna(self):
        return round(sum(self.dane) / len(self.dane), 3)

    def srednia_geometryczna(self):
        iloczyn = 1
        for liczba in self.dane:
            iloczyn *= liczba
        return round(iloczyn ** (1 / len(self.dane)), 3)

    def mediana(self):
        sorted_dane = sorted(self.dane)
        srodkowy_index = len(sorted_dane) // 2

        if len(sorted_dane) % 2 == 0:
            return (sorted_dane[srodkowy_index - 1] + sorted_dane[srodkowy_index]) / 2
        else:
            return sorted_dane[srodkowy_index]

    def moda(self):
        czestosci = {x: self.dane.count(x) for x in set(self.dane)}
        moda = max(czestosci, key=czestosci.get)
        return moda

    def odchylenie_standardowe(self):
        srednia = self.srednia_arytmetyczna()
        suma_kwadratow_roznicy = sum((x - srednia) ** 2 for x in self.dane)
        wariancja = suma_kwadratow_roznicy / len(self.dane)
        odchylenie_std = wariancja ** 0.5

        return round(odchylenie_std, 3)

    def wspolczynnik_korelacji(self, other):
        if len(self.dane) != len(other.dane):
            raise ValueError("Długość danych musi być taka sama")

        srednia_self = self.srednia_arytmetyczna()
        srednia_other = other.srednia_arytmetyczna()

        suma_produktow_roznicy = sum((x - srednia_self) * (y - srednia_other) for x, y in zip(self.dane, other.dane))
        suma_kwadratow_roznicy_self = sum((x - srednia_self) ** 2 for x in self.dane)
        suma_kwadratow_roznicy_other = sum((y - srednia_other) ** 2 for y in other.dane)

        wsp_korelacji = suma_produktow_roznicy / (suma_kwadratow_roznicy_self ** 0.5 * suma_kwadratow_roznicy_other ** 0.5)

        return round(wsp_korelacji, 3)

    def regresja_liniowa(self, other):
        if len(self.dane) != len(other.dane):
            raise ValueError("Długość danych musi być taka sama")

        srednia_self = self.srednia_arytmetyczna()
        srednia_other = other.srednia_arytmetyczna()

        suma_produktow_roznicy = sum((x - srednia_self) * (y - srednia_other) for x, y in zip(self.dane, other.dane))
        suma_kwadratow_roznicy_self = sum((x - srednia_self) ** 2 for x in self.dane)

        a = round(suma_produktow_roznicy / suma_kwadratow_roznicy_self)
        b = round(srednia_other - a * srednia_self)

        return a, b

def print_menu():
    print("Menu:")
    print("1. Oblicz średnią arytmetyczną")
    print("2. Oblicz średnią geometryczną")
    print("3. Oblicz medianę")
    print("4. Oblicz modę")
    print("5. Oblicz odchylenie standardowe")
    print("6. Oblicz współczynnik korelacji")
    print("7. Oblicz regresję liniową")
    print("8. Wyjście")
    print("")

def wczytaj_dane():
    print("Wybierz sposób wczytania danych:")
    print("1. Z pliku Excela (.xlsx)")
    print("2. Z pliku tekstowego (.txt)")
    print("3. Wpisane odręcznie (odzielone spacją)")

    while True:
        wybor = input("Wybierz opcję: ")
        if wybor == "1":
            nazwa_pliku = input("Podaj nazwę pliku Excela (.csv): ")
            dane = pd.read_csv(nazwa_pliku)
            return dane.values.flatten().tolist()
        elif wybor == "2":
            nazwa_pliku = input("Podaj nazwę pliku tekstowego (.txt): ")
            with open(nazwa_pliku, 'r') as plik:
                dane = plik.read().split()
                dane = [float(x.strip()) for x in dane]
            return dane
        elif wybor == "3":
            dane = [float(x) for x in input("Podaj dane oddzielone spacją: ").split()]
            return dane
        else:
                print("Niepoprawny wybór.")

def main():
    dane = wczytaj_dane()
    if len(dane) == 0:
        print()
        print("Brak danych. Spróbuj ponownie \n")
        time.sleep(1.5)
        return main()

    print("Wczytano dane: ", dane)
    time.sleep(1.4)
    statystyki = Statystyka(dane)
    print()
    print_menu()



    while True:
        wybor = input("Podaj numer operacji: ")
        if wybor == "1":
            print(f"Srednia arytmetyczna: {statystyki.srednia_arytmetyczna()}")
        elif wybor == "2":
            print(f"Srednia geometryczna: {statystyki.srednia_geometryczna()}")
        elif wybor == "3":
            print(f"Mediana: {statystyki.mediana()}")
        elif wybor == "4":
            print(f"Moda: {statystyki.moda()}")
        elif wybor == "5":
            print(f"Odchylenie standardowe: {statystyki.odchylenie_standardowe()}")
        elif wybor == "6":
            try:
                print("Podaj drugi zestaw danych: (długość danych musi być taka sama)")
                print()
                time.sleep(1.5)
                other_dane = wczytaj_dane()
                other_statystyki = Statystyka(other_dane)
                print(f"Wspolczynnik korelacji: {statystyki.wspolczynnik_korelacji(other_statystyki)}")
            except ValueError as e:
                print(e)
                return None
        elif wybor == "7":
            try:
                print("Podaj drugi zestaw danych: (długość danych musi być taka sama)")
                print()
                time.sleep(1.5)
                other_dane = wczytaj_dane()
                other_statystyki = Statystyka(other_dane)
                a, b = statystyki.regresja_liniowa(other_statystyki)
                print(f"Regresja liniowa: y = {a:.2f}x + {b:.2f}")
            except ValueError as e:
                print(e)
                return None
        elif wybor == "8":
            break
        else:
            print("Niepoprawny wybór. Wybierz ponownie.")


if __name__ == "__main__":
    main()
