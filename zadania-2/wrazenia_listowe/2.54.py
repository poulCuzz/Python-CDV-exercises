pracownicy = [("Jan Kowalski", 3200), ("Mteusz Nowak", 4500), ("Anna Kubaczyk", 5200), ("Katarzyna Nowacka", 5100), ("Władysław Marciniak", 4800)]
richEmployees = [employee for employee in pracownicy if employee[1] > 5000]
print(richEmployees)