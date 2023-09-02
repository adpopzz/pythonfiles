allusers=["mohanlal","fhad","dq","vijy","nivin","asif"]

dq_friends_list=["mohanlal","fahad","asif"]
asif_friendslist=["mohanlal","fahad","vijay","nivin"]
#suggetion
st1=set(allusers)
st2=set(dq_friends_list)

suggetion_to_dq=st1.difference(st2) 
suggetion_to_dq.remove("dq")

# print(suggetion_to_dq)
mutual_friends=set(asif_friendslist).intersection(dq_friends_list)

print(mutual_friends) 