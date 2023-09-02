items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
]

items_name=list(map(lambda it:it.get("name"),items))
# print(items_name)


lst_itemsname=[it.get("name") for it in items]
# print(lst_itemsname)
price=list(map(lambda it:it.get("price"),items))
# print(price)
price_lst=[it .get("price") fot it in items]
print(price_lst)