#num=1634 (1**4+6**4+3**4+4**4)
num=1634
org=num
cnt=len(str(num))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit**cnt
    num=num//10
if(org==sum):
    print("is a amstrong number")
else:
    print("is not amstrong")