 # thread= a flow of execution. Like a seperate order of instructions
  #         however each thread takes a turn running to acheive concurrency
#           GIL=(global interpreter lock)
#          allows only one thread to hold the control of the python interpreter


#cpu bound= program/task spends most of the time waiting for internal events
#io bound= program/task spends most of the time waiting for external events


import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(5)
    print("You drink coffee")

def study():
     time.sleep(5)
     print("You finish study")

x=threading.Thread(target=eat_breakfast,args=())
x.start()

y=threading.Thread(target=drink_coffee,args=())
y.start()

z=threading.Thread(target=study,args=())
z.start()

#eat_breakfast()
#drink_coffee()
#study()
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())