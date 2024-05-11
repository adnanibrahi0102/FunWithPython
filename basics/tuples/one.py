#tuples

#how to create tuples

#tuples are immutable it can not be manipulate

tea_tuple = ("black", "blue", "green", "yellow" , "yellow")

print(tea_tuple)

# tea_tuple[0] = "lemon"
# shows error message  'tuple' object does not support item assignment
# print(tea_tuple) 


# shows count of items
print(tea_tuple.count("yellow"))


number_tuples = (1, 2, 3,4)
(one,two,three,four) = number_tuples

print(three,four)


print(tea_tuple.index("yellow"))