myDict = {
    "fast": "In a quick action",
    "slow": "In a slow action",
    "gaurav": "Third year computer engineering students",
    "python": "Programming Language",
    "marks": [68, 89, 70, 59, 97],
    1:2
}
# Dictionary Methods
print(type(myDict.keys())) #Prints the keys of dictionary
print(myDict.values()) #Prints the values of dictionary
print(myDict.items()) #Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Ritik":"Friend",
    "Krushna":"Friend",
    "Darshan":"Friend",
    "python": "Easy and Understandable Programming language"
}
myDict.update(updateDict) #Update the dictionary by adding key-value pairs form updateDict
print(myDict)

print(myDict.get("python"))  #Prints value associated with key "Gaurav"
print(myDict["python"])      #Prints value associated with key "Gaurav"

# The difference between .get and [] syntax in dictionaries?
print(myDict.get("python2"))  #Returns None as python2 is not present in the dictionary
print(myDict["python2"])      #throws an error as python2 in not present in dictionary