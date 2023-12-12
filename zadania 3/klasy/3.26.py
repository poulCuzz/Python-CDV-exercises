class Student:
    def __init__(self, imie, nazwisko, oceny):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = oceny

        def dodajOcene(self, ocena):
            self.oceny.append(ocena)
            print(f"dodano ocene {ocena} studentowi {self.imie}")

        def wypiszOceny(self):
            for ocena in self.oceny:
                print(ocena)

        def obliczSrednia(self):
            suma = 0
            for ocena in self.oceny:
                suma += ocena
            return suma / len(self.oceny)


studenci = []
def menu():
    print("Menu:")
    print("D-dodaj studenta")
    print("U-usuń studenta")
    print("O-dodaj ocenę studentowi")
    print("W-wypisz oceny studenta")
    print("S-średnia studenta")
    print("exit-wyjście z programu")
    print()

def dodajStudenta(imie, nazwisko, oceny):
    student = Student(imie, nazwisko, oceny)
    studenci.append(student)

def usunStudenta(idStudenta):
    usunietyStudent = studenci.pop(idStudenta)
    print(f"usunięto studenta o imieniu {usunietyStudent.imie}")

def dodajOcene(idStudenta, ocena):
    studenci[idStudenta].oceny.append(ocena)

def wypiszOceny(idStudenta):
    for ocena in studenci[idStudenta].oceny:
        print(ocena)

def sredniaStudenta(idStudenta):
    suma = 0
    for ocena in studenci[idStudenta].oceny:
        suma += ocena
    return suma / len(studenci[idStudenta].oceny)


menu()
usersInput = input("-> ")
while usersInput != "exit":
    if usersInput == "D":
        oceny = []
        imie = input("podaj imie: ")
        nazwisko = input("podaj nazwisko: ")
        while True:
            input2 = input("wpisz ocene: ")
            if input2 == "end":
                break
            else:
                oceny.append(float(input2))
        dodajStudenta(imie, nazwisko, oceny)
        menu()
        usersInput = input("-> ")
    elif usersInput == "U":
        idStudenta = int(input("podaj id studenta: "))
        usunStudenta(idStudenta)
        menu()
        usersInput = input("-> ")
    elif usersInput == "O":
        idStudenta = int(input("podaj id studenta: "))
        ocena = float(input("podaj ocene: "))
        dodajOcene(idStudenta, ocena)
        print("Dodano ocenę pomyślnie")
        menu()
        usersInput = input("-> ")
    elif usersInput == "W":
        idStudenta = int(input("podaj id studenta: "))
        wypiszOceny(idStudenta)
        menu()
        usersInput = input("-> ")
    elif usersInput == "S":
        idStudenta = int(input("podaj id studenta: "))
        print(f"Średnia studenta: {sredniaStudenta(idStudenta)}")
        menu()
        usersInput = input("-> ")



