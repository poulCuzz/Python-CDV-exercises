# Zadanie 2.11
#
# Utwórz program, który wykorzystując słownik, będzie pobierać od użytkownika numer miesiąca, a wyświetlać na ekranie będzie jego nazwę w formie tekstowej.

months = {
          1: "styczen",
          2: "luty",
          3: "marzec",
          4: "kwiecien",
          5: "maj",
          6: "czerwiec",
          7: "lipiec",
          8: "sierpien",
          9: "wrzesien",
          10: "pazdziernik",
          11: "listopad",
          12: "grudzien"
          }

numOfMonth = int(input("podaj numer miesiaca: "))
print(months.get(numOfMonth))




