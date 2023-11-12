# Sito Erastotenesa: Utwórz program, który przyjmie liczbę naturalną i sprawdzi czy jest pierwsza czy nie.

num = int(input("Podaj liczbę: "))
prime = True

for i in range(2, num):
    if num % i == 0:
        print("Liczba nie jest pierwsza")
        prime = False
        break
    else:
        continue
if prime:
    print("Liczba jest pierwsza")
