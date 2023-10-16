#zip(*iterables)=aggregate elements from two or more iterables (list,tuples,sets,etc)
#                 creates a zip object with paired elements stored in tuples for each elements

usernames=["Dude","Bro","Mister"]
passwords=("p@ssword","abc123","guest")

users=zip(usernames,passwords)
print(type(users))
users=list(users)
for i in users:
    print(i)



users=dict(users)

for key,value in users.items():
    print(key+":"+value)
