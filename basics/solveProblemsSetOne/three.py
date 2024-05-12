marks  = 80
if(marks>=101):
    print("Invalid Marks")
    exit(1)

if(marks>=90):
    grade = "A"
elif(marks>=80):
    grade = "B"
elif(marks>70):
    grade = "C"
elif(marks>60):
    grade = "D"
else:
    grade = "F"

print("Grade: " + grade)