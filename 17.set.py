#set = collection of elements which is unordered, unindexed. No duplicate values

utensils={'fork','spoon','knife'}
dishes={'bowl','plate','cup'}

utensils.remove("fork")
utensils.add('Napkin')
#utensils.clear()
utensils.update(dishes) #all elements of dishes are updated to utensils
dinner_table=utensils.union(dishes)

for x in utensils:
    print(x)

for i in dinner_table:
    print(i)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))