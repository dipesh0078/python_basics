#tuple=collection which is ordered and unchangeable
#       used to group together related data


student=("Bro",21,'male')

print(student.count("Bro"))
print(student.index('male'))

for i in student:
    print(i)

if 'Bro' in student:
    print("Bro is here")