#Movie ticket pricing

# Question Movie tickets are priced based on age $12 for adults (18 or above) $8 for children everyone gets $2 dicount on wednesday


age= 23

day = "Wed"

price = 12 if age>= 18 else 8
if(day == "Wed"):
    price = price -2

print("Ticket Price for you is $",price)