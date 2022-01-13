# Q.5 Repeat program 4 for a list of such words to be censored.
words = ["fruits", "flowers", "vegatables"]
with open("sample.txt") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "popkon")

with open("sample.txt", "w") as f:
    f.write(content)