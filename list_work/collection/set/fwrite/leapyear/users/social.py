f=open("C:\\Users\\silverline\\Desktop\\my_pythoncode\\list_work\\collection\\set\\fwrite\\leapyear\\users\\data.txt","r")

users=[]

for line in f:
    text=line.rstrip("\n")
    name,followers,following=text.split(",")
    print(name)
    print(followers)
    print(following)