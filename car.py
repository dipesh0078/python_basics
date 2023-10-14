class Car:
    
    def __init__(self,make,model,year,color):
        self.make=make #instance variable=declare inside constructor
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print("Car is "+self.model+" driving")
    def stop(self):
        print("car stoped")