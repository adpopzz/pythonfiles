import re
sent="hi hi hello hi  hello inwhile sir mam"
# # ct=sent.count("hi")
# print(ct)
ct=re.findall("hi",sent)
print(len(ct))