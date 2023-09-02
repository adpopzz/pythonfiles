fread=open("C:\\Users\\silverline\\Desktop\\my_pythoncode\\list_work\\collection\\set\\fwrite\\years.txt","r")

fwrite=open("C:\\Users\\silverline\\Desktop\\my_pythoncode\\list_work\\collection\\set\\fwrite\\leapyears.txt","w")

for line in fread:
    year=int(line.rstrip("\n"))

    if(year%100==0 and year%400==0):
        fwrite.write(str(year)+"\n")
    elif(year%100!=0 and year%4==0):
        fwrite.write(str(year)+"\n")
print("finished")