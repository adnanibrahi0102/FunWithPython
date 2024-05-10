tea_varities = ["black","green","oolang","white"]
print(tea_varities)
# slicing
print(tea_varities[2:4])
tea_varities[3]="herbal"
print(tea_varities)
print(tea_varities[1:2])
tea_varities[1:2] = ["lemon"]
print(tea_varities)
tea_varities[1:2]=["green","masala"]
print(tea_varities)
tea_varities.append("lipton")
tea_varities.insert(3,"nooonChai")

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)
if "lipton" in tea_varities:
      for tea in tea_varities:
          print(tea, end = "-")
else:
     print("No tea varities found")



y = range(10)
print(y)

squared_numbers = [x**2 for x in y]
print(squared_numbers)

cube_nums = [y**3 for y in range(20)]
print(cube_nums)

array_nums = [x**2 for x in range(10)]
print(array_nums)
target = 25
for i in array_nums:
     if i ==target:
          print("target found")
          break
     else:
          print("target not found")
          break