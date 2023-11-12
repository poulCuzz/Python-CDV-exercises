data = []

while True:
    print("Wybierz z pośród trzech opcji wpisując 'D'(dodaj) / 'P' (pokarz) / 'K' (koniec)")
    letter = input("Your choice: ")
    match letter:
        case "D":
            name = input("Wprowadź swoje imię: ")
            surname = input("Wprowadź swoje nazwisko: ")
            phone_number = input("Wprowadź swój nr tel.: ")
            data.append(name)
            data.append(surname)
            data.append(phone_number)
        case "P":
            print(data)
        case "K":
            break
