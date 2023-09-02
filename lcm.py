num1=12
num2=24                            #lcm(a,b)=(a*b)/gcd(a,b)
gcd=1
for i in range(1,12+1):
    if((num1%i==0)and(num2%i==0)):
        gcd=i
lcm=(num1*num2)/gcd
print("lcm",lcm)
print("gcd",gcd)
        
