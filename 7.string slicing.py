#slicing= create a substring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]


name="Bro Code"

first_name= name[0:3]
last_name=name[4:8]
print(first_name)
print(last_name)

step_using= name[0:8:2]
print(step_using) 

reversed_name= name[::-1]
print(reversed_name)



#slice function

website='http://google.com'
slice=slice(7,-4,1)
print(website[slice])