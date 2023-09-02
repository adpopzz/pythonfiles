from re import  *
rule="[k-m][369][a-zA-z0-9]*"
var_name="k3llo"
macher=fullmatch(rule,var_name)

if macher!=None:
    print("valid")
else:
    print("not valid")