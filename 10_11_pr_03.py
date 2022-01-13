# Q.3 Create a class with a class attribute a : create an object from it and set a directly using object a = 0. Does this change the class attribute?
class Sample:
    a = "Gaurav"

obj = Sample()
obj.a = "Prasad"
# Sample.a = "Prasad"

print(Sample.a)
print(obj.a)