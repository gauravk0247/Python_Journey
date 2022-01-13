# Q.4 Add a static method in problem 2 to greet the user with hello.
class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareroot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

    @staticmethod
    def greet():
        print("********** Hello there welcome to the best calculator of the world **********")

a = calculator(int(input("Enter a Number: ")))
a.greet()
a.square()
a.squareroot()
a.cube()