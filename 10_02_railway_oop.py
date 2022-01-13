# import pandas as pd

class RailwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

gauravApplication = RailwayForm()
gauravApplication.name = "Gaurav"
gauravApplication.train = "Rajdhani Express"
gauravApplication.printData()