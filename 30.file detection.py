import os

path="C:\\Users\\Legion\\Desktop\\text.txt"

if os.path.exists(path):
    print("Location exist")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is directory")
else:
    print("The location doesn't exist")

