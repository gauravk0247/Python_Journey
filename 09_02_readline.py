f = open('sample.txt')
data = f.readline()
print(data)

# Read first line ....
data = f.readline()
print(data)

# Read second line ....
data = f.readline()
print(data)

# Read fourth line .... and so on ....
data = f.readline()
print(data)
f.close()