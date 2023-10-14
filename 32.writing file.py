text="This is added from a code\n enjoy "
text2="this is added"

with open("C:\\Users\\Legion\\Desktop\\text.txt",'w') as file:
    file.write(text)


with open("C:\\Users\\Legion\\Desktop\\text.txt","a") as file:
    file.write(text2)