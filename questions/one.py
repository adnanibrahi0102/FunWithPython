def arithmetic_operations():
    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))
    operator = input("Enter operator: ")

    match operator:
        case "+":
            print(num_1 + num_2)
        case "-":
            print(num_1-num_2)
        case "/":
            print(num_1 / num_2)
        case "*":
            print(num_1 * num_2)
        case _:
            print("Invalid Input")


arithmetic_operations()