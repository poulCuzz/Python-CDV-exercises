print("What operation you choose?")
print("- write '+' to choose addition")
print("- write '-' to choose subtraction")
print("- write '*' to choose multiplication")
print("- write '/' to choose division")
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
            print(numbers[0] / numbers[1])
    except ValueError:
        print("wrong type of value, try again...")
        numbers = []
    else:
        break

