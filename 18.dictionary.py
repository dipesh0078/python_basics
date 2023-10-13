#dictionary= A changeable, unordered collection of unique key: value pairs
#              fast beacuse they use hashing, allow us to access a value quickly

capitals={'USA':'Washington DC',
          "India":"New Delhi",
          "China":"Beijing",
          "Russia":'Moscow'}

print(capitals["Russia"])
print(capitals.get("Germany"))
#return none is it is not present
print(capitals.keys())
print(capitals.values())

#changing values
capitals.update({"Nepal":"Kathmandu"})

capitals.pop("China")
#capitals.clear()
for key,value in capitals.items():
    print(key,value)
