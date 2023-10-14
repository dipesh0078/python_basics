try:
    with open("C:\\Users\\Legion\\Desktop\\texth.txt") as file:
         print(file.read())
except Exception:
     print("file not found")

