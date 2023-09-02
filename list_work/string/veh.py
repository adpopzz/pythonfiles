from re import *

rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9-]{4}"
reg_num="KL-33-ab-6838"
matcher=fullmatch(rule,reg_num)
print("valid"if matcher!=None else "invalid")