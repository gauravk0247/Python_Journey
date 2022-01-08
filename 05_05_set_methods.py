# Creating an empty set
b = set()
print(type(b))

# Adding values to an empty set
b.add(2)
b.add(3)
b.add(3)  #Adding a value repeatdly does not changes a set
b.add((4, 5, 6))

## Accessing Elements
# b.add({4:5})  #Cannot add list or dictionary to sets
print(b)

## length of the set
print(len(b)) #Prints the length of this set
 
## Remove of an Item
b.remove(2) #Removes 2 from set b
# b.remove(12) #throws an error while trying to remove 12(which is not present in set)
print(b)

## Remove a Random number in a set 
print(b.pop())

## Clear to all set values
b.clear()
print(b)

## Union 
b.union()
print(b)

## Intersection
b.intersection()
print(b)