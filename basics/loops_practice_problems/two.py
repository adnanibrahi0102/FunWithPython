# sum of even numbers
n = 10
sum = 0
for i in range(1, n+1):
    if(i % 2 == 0):
        sum += 1

print(sum)

# table
number = 39

for i in range(1, 11):
    if(i==5):
        continue
    print(number, 'x', i, '=', number * i)
