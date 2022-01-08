# Q. Write a program to create a dictionary of Hindi words with values as their english translation provide user with an option to look it up!
myDict = {
    "Pankha": "fan",
    "khurchi":"chair",
    "lamb":"long"
}
print("OPtions are ", myDict.keys())
a = input("Enter the Hindi word\n")
# print("The meaning of your word is:", myDict[a])

# Below line will not throw an error if the key is not present
print("The meaning of your word is:", myDict.get(a))