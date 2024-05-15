#find the first non-repeated character

input_string = "areetmckpwwaighhrw"

for char in input_string:
    if(input_string.count(char)) == 1:
        print("Char is : " , char)
        break