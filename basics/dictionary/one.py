chai_types ={"masala": "spicy","ginger":"zesty","green":"fresh"}
print(chai_types)
print(chai_types.get("masala"))
for chai in chai_types:
    print(chai,chai_types[chai])


for key ,value in chai_types.items():
    print(key,value)

square_nums = {x:x**2 for x in range(10)}
print(square_nums)


