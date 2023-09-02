#sen="joel is a very good student in may batch"
#word=sen.split(" ")
# bol=sen.startswith("joel")
# if bol==True:
#     print("the sentence is start with 'joel")
# if word[0]== ("joel"):
#     print("the sentence is start with 'joel'")

import re
sen="joel is a very good student in may batch"
# x=re.search("^is",sen)
# y=re.search("^joel",sen)
# en=re.search("joel$",sen)
# print(x)
# print(y)
# print(en)
st_en=re.search("^joel.*batch$",sen)
print(st_en)
# se=re.search("^is",sen) ,re. search("joel$",sen)
# print(se)