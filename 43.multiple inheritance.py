#multiple inheritance= when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")

class Predetor:

    def hunt(self):
        print("This animal is hunting")
             
class Fish(Prey,Predetor):#multiple inheritance
      pass

class Rabbit(Prey):
    pass

class Hawk(Predetor):
    pass


rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()