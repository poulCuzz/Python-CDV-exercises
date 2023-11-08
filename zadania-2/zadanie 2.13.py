# Zadanie 2.13
#
# Korzystając z informacji zawartych na stronie:
# https://pl.wikipedia.org/wiki/Rzymski_system_zapisywania_liczb
# utwórz program, który zamieni cyfrę rzymską na arabską (do 1000).

romanArabic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
romanNum = input("podaj liczbe rzymska: ")

numList = []
for i in range(0, len(romanNum)):
    numList.append(romanArabic.get(romanNum[i]))

value = 0
for i in range(0, len(romanNum)):
    value = value + romanArabic.get(romanNum[i])

originalList = numList.copy()
numList.sort()
numList.reverse()


if originalList == numList:
    print(f"przekształcone na arabskie: {value}")
else:
    for i in range(0, len(originalList)):
        if i < len(originalList) - 1:
            if originalList[i] < originalList[i + 1]:
                originalList[i] = -originalList[i]
        else:
            break
    value = 0
    for i in range(0, len(originalList)):
        value += originalList[i]
    print(f"przekształcone na arabskie: {value}")











