# Q.4 Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n == 1 or n == 0:
        return n
    return n + sum(n-1)

s = sum(16)
print(s)