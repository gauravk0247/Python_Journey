# Q.1 Create a class programmer for storing information of two programmers working at microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

gaurav = Programmer("Gaurav", "Skype")
prasad = Programmer("Prasad", "GitHub")
gaurav.getInfo()
prasad.getInfo()