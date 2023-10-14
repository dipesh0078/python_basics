#copyfile()= copies contents of a file
#copy()= copyfile()+permission mode+ destination can be directory
#copy2()= copy()+copies metadata (file's creation and modification times)


import shutil

shutil.copyfile("C:\\Users\\Legion\\Desktop\\text.txt","C:\\Users\\Legion\\Desktop\\copy.txt") #src, destination