"""
print() to display message in console
type() 
input() to read message from console
function are use to performe a specific task
"""
# num1=input("to say hello:")
# print(num1)

# create a add function

# def add(a1,a2):
#     res=a1+a2
#     return res
# print(add(100,20))

# create a function mult with three parameter

# def mult(a1,a2,a3):
#     res=a1*a2*a3
#     return res
# print(mult(3,4,1))

#create a function max_two with two parameter that return largest number

def max_two(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
print(max_two(20,25))