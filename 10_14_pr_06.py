# Q.6 cam you change the self parameter inside a class to something else (say "gaurav"). Try changing self to 'slf' or 'gaurav' and see the effects.
class Sample:
    def __init__(self, name):
        self.name = name

obj = Sample("Gaurav")
print(obj.name)