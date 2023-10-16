#higher order function= a function that either:
#                       1.accepts a function as an argument
#                         or returns a function
#              (in python, functions are also treated as objects)

 

#1st
def loud(text):
    return text.upper()

def quit(text):
    return text.lower()

def hello(func):
    text=func("Hello")
    print(text)


hello(loud)
hello(quit)

#2nd
def divisor(x):
     def dividend(y):
         return y/x
     return dividend

divide=divisor(2)
print(divide(10))