#exception = event detected during executed that interrupt the flow of program


try:
    numerator=int(input("Enter a number to divide: "))
    denominator=int(input("Enter a number to divide by: "))
    result=numerator/denominator
    
except ZeroDivisionError:
      print("You cant divide by zero")
except ValueError:
      print("Enter only number please")
except Exception:
       print("somthing went wrong")
else:
     print(result) #if no exception occur then this will be executed