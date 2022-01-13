# Q.1 Write a program to read the text from a given file 'sample2.txt' and find out wheather it continus the word 'sample2'.
f = open('sample2.txt')
t = f.read()
if 'python' in t:
    print("python is present")
else:
    print("python is not present")
f.close()