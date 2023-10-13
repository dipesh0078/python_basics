#nested loop = the loop inside a loop

rows=int(input("How many rows? "))
column=int(input("How many column? "))
symbol=input("Enter your symbol: ")

for i in range(rows):
    for j in range(column):
        print(symbol, end='')
    print()

    
