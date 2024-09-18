# Prompt for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculations using match case
match operation :
    case "+" :
        result = num1 + num2
        print(f"The result is {result}.")
    case "-" :
        result = num1 - num2
        print(f"The result is {result}.")
    case "*" :
        result = num1 * num2
        print(f"The result is {result}.")
    case "/" :
        result = num1 / num2
        print(f"The result is {result}.")
        if num1 | num2 >= 0 :
            print("Cannot divide by 0")
    case _:
            print("Invalid operation. Please choose one of (+, -, *, /).")