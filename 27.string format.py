#str.format()= optional method that gives users
#              more control when displaying output

animal="cow"
item="moon"

#print("The "+animal+" jumped over the "+item)

print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))
print("The {animal} jumped over the {item}".format(animal="tiger",item='mars'))

text="The {} jumped over the {}"

print(text.format(animal,item))


#add padding

name="bro"

print("My name is {}".format(name))
print("My name is {:10} and im learning".format(name))#add padding
print("My name is {:<10} and im learning".format(name))#add padding
print("My name is {:>10} and im learning".format(name))#add padding
print("My name is {:^10} and im learning".format(name))#add padding


number=3.14159
num=1000000
print("the number pi is {:.2f}".format(number))
print("the price is ${:,}".format(num))
print("the price is ${:b}".format(num))#binary
print("the price is ${:o}".format(num))#octal
print("the price is ${:x}".format(num))#lower case hex
print("the price is ${:e}".format(num))#scientific notation