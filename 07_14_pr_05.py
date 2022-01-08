# Q.5 Write a program to find the sum of first n natural numbers using for loop.
number = int(input("Please Enter any Number: "))
total = 0

for value in range(1, number + 1):
    total = total + value

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))