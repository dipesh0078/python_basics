#map()= applies a function to each item in an iterable (list,tuple,etc)

#map(function,iterable)

store=[("shirt",20.00),
       ("pants",25.00),
       ("jacket",50.00),
       ("socks",10.00)]

to_euro=lambda data:(data[0],data[1]*0.82)
to_dollar=lambda data:(data[0],data[1]/0.82)
store_euro=list(map(to_euro,store))
for i in store_euro:
    print(i)
