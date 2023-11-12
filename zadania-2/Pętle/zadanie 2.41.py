num = int(input("podaj numer wyrazu ciągu Fibonacciego: "))
n1 = 1
n2 = 1
for i in range(3, num + 1):
    m = n1
    n1 = n2
    n2 = m + n2
if num == 0:
    print(0)
elif num == 1 or num == 2:

    print(1)
else:
    print(n2)

