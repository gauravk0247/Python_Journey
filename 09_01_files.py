# Use open function to read the context of a file! 
# f = open('sample.txt', 'r') 
f = open('sample.txt') # by default the mode is r
# data = f.read()
data = f.read(6) #reads first  6 characterform the file
print(data)
f.close()