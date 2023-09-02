import re

mob=input("enter your mobile number wi5th country code : ")
x=re.search("^[+]91",mob)
if(x):
    print("number is Indian")
else:
    print("number is foreing")

# resi=input("enter a residence number")
# ekm=re.search("^0484",resi)
# ijk=re.search("^0480",resi)
# tcr=re.search("^0487",resi)
# mpr=re.search("^0494",resi)
# ksd=re.search("^04994",resi)
# cct=re.search("^0495",resi)

# if ekm:
#     print("ekm")
# elif ijk:
#     print("ijk")
# elif tcr:
#     print("tcr")
# elif mpr:
#     print("mpr")
# elif ksd:
#     print("ksd")
# else:
#     print("cct")