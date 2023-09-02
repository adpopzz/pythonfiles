number=[2,7,8,9,12,13]

odd_list=[]
even_list=[]
for num in number:
    # even_list.append(num) if num%2==0 else odd_list.append(num)
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
        
print(even_list)
print(odd_list)

