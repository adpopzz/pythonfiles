text="England promissed to continue its aggressive approch to test cricket"
#print the words strarting with vowels
vovewls=("a","e","i","o","u")


# words=text.split()

# for w in words:
#     if w[0].casefold() in vovewls:
#         print(w)

ws=[w for w in text.split(" ") if w[0].casefold() is vovewls ]

print(ws)