# Q.8 Write a python function to print multiplication table of a given number.
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# We are using "for loop" to iterate the multiplication 10 times       
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)   


# Q. Write a program to print multiplication table of a given number using for loop.
# num = int(input("Enter a number "))
# for i in range (1, 11):
#     # print(str(num) + " X " + str(i) + "=" + str(i*num))
#     print(f"{num}X{i}={num*i}")