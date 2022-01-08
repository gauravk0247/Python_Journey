# Q.3 Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter a number "))
i = 1
while(i<11):
    print(str(num) + " X " + str(i) + "=" + str(i*num))
    i = i + 1
    # print(f"{num}X{i}={num*i}")