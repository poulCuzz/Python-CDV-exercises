while True:
    num = input("Wprowadz 5 cyfr: ")
    if num.isdigit() and len(num) == 5:
        break
    else:
        print("blad! Wprowadz poprawna liczbe")


numDictionary = {1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "piec", 6: "szesc", 7: "siedem", 8: "osiem", 9: "dziewiec", 0: "zero"}
# for i in range(0, len(num)):
#     print(numDictionary.get(int(num[i])))
myList = []
for i in range(0, len(num)):
    myList.append(numDictionary.get(int(num[i])))

print(num + " - " + myList[0] + " " + myList[1] + " " + myList[2] + " " + myList[3] + " " + myList[4])


