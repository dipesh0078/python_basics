import random


x=random.randint(1,6)
y=random.random()
print(x)
print(y)


mylist=['rock','paper','scissors']
cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
z=random.choice(mylist)
random.shuffle(cards)
print(z)
print(cards)