class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

gaurav = Employee()
gaurav.salary = 100000
gaurav.getSalary() # Employee.getSalary(gaurav)

# class student:
#     branch = "Computer"
#     def getStudent(self):
#         print("Student is regular")

# gaurav = student()
# gaurav.getStudent()