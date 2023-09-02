expenses=[20000,25000,35000,360000,10000]


# for exp in expenses:
#     print(exp)

for exp in expenses:
    if exp >16000:
        print(exp)

max_exp=max(expenses)

min_exp=min(expenses)

sum_exp=sum(expenses)

print(max_exp,min_exp,sum_exp)