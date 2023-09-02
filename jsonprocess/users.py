from json import load
with open("C:\\Users\\silverline\\Desktop\\my_pythoncode\\jsonprocess\\data.json","r") as f:
    data= load(f)

    # print(data)

# names=[u.get("name") for u in data]
# print(names)

# print(max(data,key=lambda s:s.get("total")))

# out=sorted(data,key=lambda s:s.get("total"),reverse=True)
# print(out)

bca_students=[u.get("name") for u in data if u.get("course")=="bca"]
print(bca_students)