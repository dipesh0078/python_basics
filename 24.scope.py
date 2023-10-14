#scope= The region that a variable is recognized
#          A variable is only available from inside the region it is created
#          A global and locally scoped versions of a variable can be created



name="Thapa"  #global deceleration (available inside and outside functions)

def display():
    #name="Dipesh"  #local decleration (availabe only inside this function)
    print(name)

display()
print(name)