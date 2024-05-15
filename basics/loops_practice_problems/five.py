# keep asking user input until they enter number b/w 1 -10

while True:
  number = int(input("Enter number Between 1 - 10 : "))
  if (1<= number <=10):
    print("Thanks!!")
    break
  else:
    print("Invalid Input Try Again !!")
  