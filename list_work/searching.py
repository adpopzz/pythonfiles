#linear

lst=[2,3,4,5,6,7,8,9,10]
"""
elem=15
is_found=False
for i in range(0,len(lst)):
    if elem==lst[i]:
        is_found=True
        break
print("is found" if is_found==True else "not found")
"""
#bionary

elem=11
low=0
upp=len(lst)-1
is_found=False
while (low<upp):
    mid=(low+upp)//2
    if elem==lst[mid]:
        is_found=True
        break
    elif elem > lst[mid]:
        low+=1
    elif elem < lst[mid]:
        upp-=1
print("found" if is_found==True else "not found")
    


