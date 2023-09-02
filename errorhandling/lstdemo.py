lst=[10,20,30,40,50]

locatiom=int(input("enter location to fech value from list"))

try:
    print(lst(locatiom))
except Exception as e:
    locatiom=int(input("enter location to fech value from list"))
    print(lst(locatiom))

finally:   
       print("dbcommit")
       print("file read")