
from re import *
rule="[a-zA-Z][a-zA-Z0-9_$]{0,10}"
ja_var="num_one$"

matcher=fullmatch(rule,ja_var)
print("invalid" if matcher==None else "valid")
