text="ABBAACD"
wc={}

for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
# print(wc)

wc={'A': 3, 'B': 2, 'C': 1, 'D': 1}

# print(max(wc,key= lambda key:wc.get(key)))
print(min(text,key=lambda key:wc.get(key)))

