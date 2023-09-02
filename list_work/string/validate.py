# import re  
# # text="aaaabbbccc"
# # text1="abcabc"
# # t=re.search("[a]{4}",text)
# # t1=re.search("[a]{4}",text1)
# # print(t)
# # print(t1)
# text="abcd5678"
# t3=re.search("[a-z]{5}",text)
# print(t3)

import re
stri="abADG1234"
s=re.search("[a-z]{2}[A-Z]{4}",stri)
print(s)