num = int(input("podaj liczbę: "))
result = 1
for i in range(1, num + 1):
    result *= i
if num == 0:
    print(1)
else:
    print(result)
    