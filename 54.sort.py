#sort() method=used with lists
#sort()function=used with iterables

students=["ram","hari","dipesh","prasanna","ayush"]
#sort() works for list if there is tuple it wont work
students.sort()
for i in students:
    print(i)

students.sort(reverse=True)
for i in students:
    print(i)

student=("ram","hari","dipesh","prasanna","ayush")
sorted_student=sorted(student) #using function for tuple
for i in sorted_student:
    print(i)

sorted_student=sorted(student,reverse=True)
for i in sorted_student:
    print(i)

print("----------------------------------------------------")
#list of tuple:
#there we can see row and column
person=[("Squidward","F",60),
        ("Sandy","A",33),
        ("Spongebob","B",20),
        ("Mr.Krabs","C",78)]

person.sort()#sorting by 1st column parameter
for i in person:
    print(i)
print("----------------------------------------------------")
#sorting by 2nd column
grade=lambda grades:grades[1]
person.sort(key=grade)
for i in person:
    print(i)

age=lambda ages:ages[2]
person.sort(key=age)
print("----------------------------------------------------")
for i in person:
    print(i)