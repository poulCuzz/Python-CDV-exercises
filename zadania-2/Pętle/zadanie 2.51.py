#Napisz program, który przyjmie od użytkownika pewną ilość liczb (uzytkownik decyduje ile),
# a następnie dokona ich sortowania.
# Zadanie wykonać nie korzystając z metody sort
# (należy samodzielnie zaprojektować algorytm sortowania).

numbers = []
while True:
    num = input("Podaj liczbę: ")
    if num == "end":
        break
    numbers.append(int(num))

sortedList = []
smallest = numbers[0]
while len(numbers) > 0:
    for i in range(len(numbers)):
        smallest = numbers[0]
        if numbers[i] < smallest:
            smallest = numbers[i]
    sortedList.append(smallest)
    numbers.remove(smallest)

print(sortedList)



