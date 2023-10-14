#*args= parameter that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments


def add(*args):
    sum=0
    args=list(args) #tuple to list the on;y we can change
    args[0]=100
    for i in args:
        sum=sum+i
    return sum

print(add(1,2,3,4,5,6))