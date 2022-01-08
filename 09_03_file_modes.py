## w = write mode
# f = open('another.txt', 'w')
# data = f.write("Nice Job Gaurav! ")

## a = append mode
# f = open('another.txt', 'a')
# data = f.write(" I am appending ! ")

# print(data)
# f.close()

## w = write mode
f = open('another.txt', 'w')
f.write(" I am writing ")
f.write(" I am writing ")
f.write(" I am writing ")
f.write(" I am writing ")
f.write(" I am writing ")
f.close()

# Sample Program
f = open('sample2.txt', 'w')
f.write("This is a python tutorial.\n")
f.write("This is a python tutorial.\n")
f.write("This is a python tutorial.\n")
f.close()