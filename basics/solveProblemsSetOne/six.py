password = "adnk873lkd"

if(len(password)<6):
    strength = "weak"
elif(len(password)<=10):
    strength = "medium"
else:
    strength = "strong"
print("Password strength is ", strength)