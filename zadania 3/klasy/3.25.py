class Employee:
    def __init__(self, name, surname, email, phoneNumber):
        self.name = name
        self.surname = surname
        self.email = email
        self.phoneNumber = phoneNumber


employees = []
name = input("name: ")
surname = input("surname: ")
email = input("email: ")
phoneNumber = input("phoneNumber: ")
newEmployee = Employee(name, surname, email, phoneNumber)

employees.append(newEmployee)

for i in range(len(employees)):
    print(employees[i].surname)
