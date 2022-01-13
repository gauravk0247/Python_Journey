# Q.6 Write a program to print log file and find out wheather it contains 'python'
with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("Python is not present")