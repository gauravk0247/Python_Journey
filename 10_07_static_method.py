class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    
    @staticmethod
    def greet():
        print("Good Morining, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the Morning")

gaurav = Employee()
gaurav.salary = 100000
gaurav.getSalary("Thanks!") # Employee.getSalary(gaurav)
gaurav.greet()
gaurav.time() # Employee.greet()