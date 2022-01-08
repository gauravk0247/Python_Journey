# Q.6 Write a python function which converts inches to cms.
def cms(inches):
    return  (inches * 2.54)
c = int(input("Enter a Value: "))
i = cms(c)
print("cms is " + str(i))