def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks [3] + marks[4])/500)*100
    return p

marks4 = [45, 78, 86, 77, 98]
percentage1 = percent(marks4)

marks5 = [75, 68, 56, 47, 38]
percentage2 = percent(marks5)
print(percentage1, percentage2)


# marks = [56, 78, 90, 65, 49]
# average = (sum(marks)/500)*100
# print(average)

# marks2 = [46, 88, 98, 75, 39]
# average = (sum(marks2)/500)*100
# print(average)

# marks = [46, 58, 68, 75, 89]
# average =((marks[0] + marks[1] + marks[2] + marks [3] + marks[4])/500)*100
# print(average)