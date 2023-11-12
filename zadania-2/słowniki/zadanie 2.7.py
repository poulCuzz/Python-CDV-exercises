dane = (1, 1, 3, 2, 4, 6, 5, 3, 2, 1, 6, 50, 2, 3)
print(len(dane))
print(dane.count(1) + dane.count(2) + dane.count(3))
if 50 in dane:
    print("Krotka zawiera 50")
else:
    print("Krotka nie zawiera 50")

