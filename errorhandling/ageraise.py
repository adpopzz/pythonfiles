age=int(input("emter age"))

if age<18:
    raise Exception("invalid age")
else:
    print("valid")