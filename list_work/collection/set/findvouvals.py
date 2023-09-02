word="missunderstand" 
# for ch in word:
    # print(ch)
vowels=["a","e","i","o","u"]
v_count=0
c_count=0
for ch in word:
    if ch in vowels:
        v_count+=1
       
    else:
        c_count+=1
            
        
print(f"vowels count={v_count}, concenent count={c_count}")

#find concenent count