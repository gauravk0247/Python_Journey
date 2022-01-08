# Q.7 Write a python function to remove a given word from a string and strip if at the same time.

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "        Gaurav is hardworker    "
n = remove_and_split(this, "Gaurav")
print(n)
# print(this.strip())