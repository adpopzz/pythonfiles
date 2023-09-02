stu_name=[]
print(stu_name)
length=int(input("enter the size of list :"))

for i in range(length):
    name=input(f"enter {i}th name of the list :")
    stu_name.append(name)
ch_name=input("enter a name :")
flag=0
for s in range(length):
    if(stu_name[s]==ch_name):
        stu_name[s]="anamika"
        flag=1
if(flag==0):
    stu_name.insert(1,"amal")
    # elif (s==length-1):
    #     stu_name.insert(1,"amal")
print(stu_name)