# num=10

# # print("+ve" if num>0 else "0ve")
# print("odd" if num%2!=0 else "even")


# num1=10
# num2=20
# print(num1 if num1>num2 else num2)

# def max_two(n1,n2):
#     return n1 if n1>n2 else n2
# print(max_two(100,200))

# def min_two(n1,n2):
#     return n1 if n1<n2 else n2
# print(min_two(100,200))

"""
            h.w
create a function max_three with three parameter of three numbers

"""
# def max_three(n1,n2,n3):
#     # if n1>n2 and n1>n3:
#     #     return n1
#     # elif n2>n3: 
#     #     return n2
#     # else:
#     #     return n3
#         return n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
#     # return n1 if (n1>n2) and (n1>n3) else (n2>n1) and (n2>n3) or n3 (n3>n1) and (n3>n2)
# print(max_three(10,40,30))


def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

n1=int(input("enter num1:"))
n2=int(input('enter num2:'))
print(smart_sub(n1,n2))
