
# This function takes input from the user for the first number
def user_number_1():
    number1 = input("Please enter first number : ")
    return number1


# This function takes the operator that needs to be applied to the numbers
def user_operator():
    operator = input("Please select the operation you would like to apply. "
                     "Enter from following numbers\n"
                     "1 : Add\n"
                     "2 : Subtract\n"
                     "3 : Multiply\n"
                     "4 : Divide\n")
    return operator


# This function takes input from the user for the second number
def user_number_2():
    number2 = input("Please enter second number : ")
    return number2

# This is the main function that performs the calculation
def evaluate(number1,operator,number2):
    result = 0
    if operator == 1:
        result = number1 + number2
    elif operator == 2:
        result = number1 - number2
    elif operator == 3:
        result = number1 * number2
    elif operator == 4:
        result = number1 / number2
    else:
        msg = "Incorrect operator"
        print(msg)
    print(str(result))
    return result


# This is the function that runs the main calculator app using the functions we created above
def main():
    number1 = int(user_number_1())
    operator = int(user_operator())
    number2 = int(user_number_2())
    evaluate(number1, operator, number2)


if __name__ == "__main__":
    main()

