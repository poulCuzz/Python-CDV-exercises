base = int(input("podaj podstawę potęgi: "))
exponent = int(input("podaj wykładnik potęgi: "))
result = 1
for i in range(1, exponent + 1):
    result *= base
print(result)
