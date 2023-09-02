birds=["peacock","pegion","duck","hen"]
ch_birds=input("enter name of bird :")

# for i in range(len(birds)-2):
#     print(i)
#     birds.remove(birds[i])
# print(birds)

for i in birds:
    if i==ch_birds:
     birds.remove(i)
print(birds)