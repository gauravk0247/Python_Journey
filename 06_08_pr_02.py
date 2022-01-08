# Q.Write a program to find out wheather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 Subjects and take marks as an input from the user.
sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail beacause you have less than 33% in one of the subjects")

if(sub1 + sub2 + sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congraluations! You pass the exam")