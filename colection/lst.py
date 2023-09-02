lst=[1,2,3,4,5]


# square=list(map(square,lst))
square=list(map(lambda n:n**2,lst))
#print(square)


cubes=list(map(lambda num:num**3,lst))
# print(cubes)

evens=list(filter(lambda n: n%2==0,lst))
# print(evens)
odds=list(filter(lambda n:n%2!=0,lst))
# print(odds)

greater_than3=list(filter(lambda n:n>3,lst))
print(greater_than3)