# def factorial(num):
#     fact=1
#     for i in range(1,(num+1)):
#         fact*=i
#     return fact
# print(factorial(5))

def prime(num):
    is_prime=True
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
    if(is_prime==True):
        return "prime"
    else:
        return "not a prime"
print(prime(100))