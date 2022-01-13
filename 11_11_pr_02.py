# Q.2 Create a class pets form a class Animals and further create class Dog from Pets. Add a method bark to class dog.
class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
d.bark()