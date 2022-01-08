# Q. If names of two friends are same; What will to the program in Problem 6?
favlanguage = {}
a = input("Enter Your Favourite language\n")
b = input("Enter Your Favourite language\n")
c = input("Enter Your Favourite language\n")
d = input("Enter Your Favourite language\n")

favlanguage['gaurav'] = a
favlanguage['gaurav'] = b # If the name are same then print the latest values
favlanguage['prasad'] = c
favlanguage['krishna'] = d
print(favlanguage)