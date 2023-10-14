#**kwargs= parameter that will pack all argumnets into a dictionary
#          useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello "+kwargs["first"]+" "+kwargs['last'])
    print("Hello ",end='')
    for ket,value in kwargs.items():
        print(value,end=' ')



hello(first="Dipesh",middle="nanan",last="thapa")