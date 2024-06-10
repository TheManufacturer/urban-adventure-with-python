def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if x == 0 or y == 0:
        print("Division by 0 not possible")
    else:
        return x / y


def main():
    number1 = 0
    number2 = 0
    print("Select an operator : ")
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    selection = input("Selection :")

    if selection in ['1', '2', '3', '4']:
        number1 = float(input("Insert first number"))
        number2 = float(input("Insert second number"))

    if selection == '1':
        print("Result : ", addition(number1, number2))

    elif selection == '2':
        print("Result : ", subtraction(number1, number2))

    elif selection == '3':
        print("Result : ", multiplication(number1, number2))

    elif selection == '4':
        print("Result : ", division(number1, number2))

    else:
        print("Not Valid Choose... :( ")


if __name__ == "__main__":
    main()
