employee={"id":100,"name":"vijay","department":"hr","salary":250000}

# def get_name(emp):
#     return emp.get("name")
# print(get_name(employee))

# get_name=lambda emp:emp.get("name")
# print(get_name(employee))

get_name=lambda emp:emp.get("salary")
print(get_name(employee))