# problem solving

# Question one : age group categorization problem ---> classify a persons age group : child (<13),teenager(13-19),adult(20-59)senior(60+)


user_age = int(input("Enter age group "))

if (user_age<13):
        print("You are a Child")
elif(user_age <20):
        print("You are a teen ager")
elif(user_age<59):
        print("You are a adult")
else:
        print("your are a senior")


