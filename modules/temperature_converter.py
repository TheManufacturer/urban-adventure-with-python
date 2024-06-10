def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32


def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)


def main_temp():
    print("Select a Converter :")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    selection = input("Type choose")

    if selection == '1':
        celsius = float(input("Type Celsius grade "))
        print("The converted value is : ", celsius_to_fahrenheit(celsius), "°")
    elif selection == '2':
        fahrenheit = float(input("Type Fahrenheit grade "))
        print("The converted value is : ", fahrenheit_to_celsius(fahrenheit), "°")
    else:
        print("Sure are u write correct test ?")


if __name__ == "__main__":
    main_temp()
