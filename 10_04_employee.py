class Employee:
    company = "Google"

gaurav = Employee()
ritik = Employee()
print(gaurav.company)
print(ritik.company)
Employee.company = "YouTube"
print(gaurav.company)
print(ritik.company)