import re
mail=input("enter the mail :")
g=re.search ("@gmail.com$",mail)
if g:
    print(" it is a vaild one..")
else:
    print("not valid")