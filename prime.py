
# num=101
# is_prime=True

# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# if(is_prime==True):
#     print(num,"is a prime")
# else:
#     print(num,"not a prime")


num1=12
num2=24
max=0


for i in range(1,(12+1)):
    if((num1%i==0)and (num2%i==0)):
        if(max<i):
    #   (num1)and (num2)>i      
           max=i
print(max)


