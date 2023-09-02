from json import load
with open("C:\\Users\\silverline\\Desktop\\my_pythoncode\\restcountries\\rest.json",encoding="UTF-8") as f:
    data=load(f)

# print(len(data))
#print name of country
 #name_country=[n.get("name") for n in data]

# print(name_country)
# print all region names

# region_name={c.get("region") for c in data}
# print(region_name)
#print asian country name

#asian_country=[c.get("name")for c in data if c.get("region")=="Asia"]
#print(asian_country)
#printafganistan population

# for c in data:
#     if c.get("name")=="Afghanistan":
#         print(c.get("population"))
#         or

# pop_afganisthan=[c.get("population")for c in data c.get("name")=="Afghanistan"]

#indian boarders

borders=[c.get("borders")for c in data if c.get("name")=="India"][0]
#print(borders)

border_name=[c.get("name")for c in data if c.get("alpha3Code") in borders]
# print(border_name)
# currence=[c.get("currencies":{code})for c in data if c.get("name")=="india"]
#print(currence)
population_hig=max(data,key=lambda c:int(c.get("population")))
print(population_hig.get("name"))