import os

source='test.txt'
destination="C:\\Users\\Legion\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
      print("Already exists")
    else:
      os.replace(source,destination)
      print(source+" was moved")

except FileNotFoundError:
      print("file not found")