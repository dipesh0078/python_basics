#prevents a  user from creating an object of that class
#+ compels a user to override abstract methods in a child class

#abstract class= a class which contains one or more abstract methods.
#abstract method= a method that has a decleration but does not have an implementation


from abc import ABC, abstractmethod  #abc=abstract base class

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    #@abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive a car")

class Motorbike(Vehicle):
    def go(self):
        print("You ride a motorbike")



car=Car()
bike=Motorbike()

car.go()
bike.go()
#car.stop()