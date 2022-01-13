class Employee:
    company = "Google"
    salary = 100

gaurav = Employee()
ritik = Employee()

# Creating instance attribute salary for both the objects
# gaurav.salary = 300
# ritik.salary = 400
gaurav.salary = 45
print(gaurav.salary)
print(ritik.salary)

# Below line throws an error as address is not present in instance/class
# print(ritik.address)