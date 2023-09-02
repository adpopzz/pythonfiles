# lst=[2,3,4,5]

# lst.insert(1,6)
# print(lst)

#empty list create

# emplist=[]
# print(emplist)

#get size of list from user , and get each of a list from user, then add to list

# length=int(input("enter size of list:"))
# for i in range(length):
#     num=int(input(f"enter {i}th position of list:"))
#     emplist.append(num)
# max_element=max(emplist)

# emplist.insert(2,max_element+10)
# print(emplist)
#     emplist.append(num)
# print(emplist)
            
#a) create an empty list an acces all the elements from the user 
#b)add new element to 2nd  posotion of all list ,which should be add by 10


#create a list of student name,then check the particular name in the list given by the user
#if name is prest change that name to "anamika" if that particular name is not present iser "amal" to the 1 position


stu_name=[]
print(stu_name)
length=int(input("enter the size of list :"))

for i in range(length):
    name=input(f"enter {i}th name of the list :")
    stu_name.append(name)
ch_name=input("enter a name :")

for s in range(length):
    if(stu_name[s]==ch_name):
        stu_name[s]="anamika"
        break
    elif (s==length-1):
        stu_name.insert(1,"amal")
print(stu_name)

#if duplicate value are present how the value wil be chnanged if a match found or not 
#i/p=> [a,b,c,a] => ch_name =a,o/p=> [anamika,b,c,anamika]
        
        
       
        




