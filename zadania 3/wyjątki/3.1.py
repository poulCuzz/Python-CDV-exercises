print("What operation you choose?")
print("- Enter '+' for addition")
print("- Enter '-' for subtraction")
print("- Enter '*' for multiplication")
print("- Enter '/' for division")
operations = {"+", "-", "*", "/"}
while True:
    operation = input("->")
    if operation in operations:
        break
    else:
        print("wrong operation, try again")
        operation = ""

print("what numbers you want to operate with?")
numbers = []
while True:
    try:
        for i in range(2):
            numbers.append(int(input("number: ")))
        print("result:")
        if operation == "+":
            print(numbers[0] + numbers[1])
        elif operation == "-":
            print(numbers[0] - numbers[1])
        elif operation == "*":
            print(numbers[0] * numbers[1])
        elif operation == "/":
            if numbers[1] != 0:
                print(numbers[0] / numbers[1])
            else:
                print("Cannot divide by zero. Please try again")
                numbers = []
                continue
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        numbers = []
    else:
        break

