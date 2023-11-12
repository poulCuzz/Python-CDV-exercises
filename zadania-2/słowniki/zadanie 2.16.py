while True:
    num1 = input("pierwsze 4 cyfry: ")
    num2 = input("drugie 4 cyfry: ")
    if num1.isdigit() and num2.isdigit() and len(num1) == 4 and len(num2) == 4:
        break
    else:
        print("bład! Podaj poprawną parę elementów!")

set1 = set()
set2 = set()
for i in range(0, len(num1)):
    updator1 = {int(num1[i])}
    updator2 = {int(num2[i])}
    set1.update(updator1)
    set2.update(updator2)
suma = set1.union(set2)
print(f"suma zbiorow: {suma}")
wspolne = set1.intersection(set2)
print(wspolne)
set1.difference_update(wspolne)
print(f"różnica zbiorów: {set1}")

