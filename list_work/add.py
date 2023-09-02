#args position arguments takes any number of parameters type tuple

# def addition(*args):
#     return sum(args)
addition=lambda *args: sum(args)
print(addition(20,30))
print(addition(10,20,30,))

