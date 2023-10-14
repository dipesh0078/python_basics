import os
path='test.txt'

try:
    os.remove(path)

except FileNotFoundError:
       print("file not found")


#for folder os.rmdir(path)
#shutil.rmtree(path) delete a directory containing files