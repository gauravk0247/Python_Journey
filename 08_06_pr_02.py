# Q.2 Write a program using function to convert celsius to fahrenheit.

def farh(cel):
    return (cel * (9/5)) + 32
c = int(input("Enter a Value: "))
f = farh(c)
print("Fahreheit Temperature is " + str(f))