a = float(input("Enter a First side: "))
b = float(input("Enter a second side: "))
c = float(input("Enter a third side: "))

d = (a+b+c)/2
area = (d*(d-a)*(d-b)*(d-c))**0.5
print('The area of the triangle is %0.2f' %area) 