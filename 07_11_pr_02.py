# Q.2 Write a program to greet all the person names stired in a list l1 and which starts with G
# l1 = ["gaurav", "Ritik", "Prasad", "Krushna", "Gayatri", "Riya"]

l1 = ["Gaurav", "Ritik", "Prasad", "Krushna","Gayatri", "Riya"]
for name in l1:
    if name.startswith("G"):
         print("Hello " + name)