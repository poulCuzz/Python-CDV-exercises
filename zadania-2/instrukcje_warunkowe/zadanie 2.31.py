# Zadanie 2.31

import random

randomNum1 = random.randint(0, 100)
randomNum2 = random.randint(0, 100)
signs = ["+", "-", "*"]

i = random.randint(0, 2)
response = int(input(f"rozwiąż to równanie: {str(randomNum1)} {signs[i]} {str(randomNum2)} = "))
while True:
    if i == 0 and response == randomNum1 + randomNum2:
        print("Dobra odpowiedz!")
        break
    elif i == 1 and response == randomNum1 - randomNum2:
        print("Dobra odpowiedz!")
        break
    elif i == 2 and response == randomNum1 * randomNum2:
        print("Dobra odpowiedz!")
        break
    else:
        print("Błędna odpowiedz, spróbuj ponownie")
        response = int(input(f"rozwiąż to równanie: {str(randomNum1)} {signs[i]} {str(randomNum2)} = "))



