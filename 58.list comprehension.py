#list comprehension= a way to create a new list with less syntax
#                    can minic certain lambda functions, easier to read
#                    list=[expression for item in iterable]

squares=[]                #create a empty list
for i in range(1,11):     #create a for loop 
    squares.append(i*i)   #define what each loop iteration should do

print(squares)


square=[i*i for i in range(1,11)]
print(square)
