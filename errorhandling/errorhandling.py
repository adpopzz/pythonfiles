num1=int(input("enter value for number"))

num2=int(input("enter value for num2"))


try:
    res=num1/num2

    print("result",res)

except Exception as e:
    print(e.args)

print("dbcommit")
print("file read")