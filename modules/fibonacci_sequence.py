def fibonacci_sequence(n_start):
    """
    Generate a sequence of Fibonacci numbers up to n_start elements.

    If n_start is less than or equal to 0, returns an error message.
    Otherwise, it returns a list containing the first n_start numbers in the Fibonacci sequence.

    :param n_start: The number of elements in the Fibonacci sequence to generate.
    :return: A list of Fibonacci numbers or an error message if n_start is <= 0.
    """

    if n_start <= 0:
        return "Are you sure that number is positive ?"
    else:
        number_sequence = []
        a, b = 0, 1
        for _ in range(n_start):
            number_sequence.append(a)
            a, b = b, a + b
        return number_sequence


def main_fib():
    """
    Prompts the user to input a number, n_start, and generates the Fibonacci sequence up to n_start elements.
    If n_start is not positive, it displays an error message. Otherwise, it prints the sequence.
    """

    print("Hello my friends... This is the Fibonacci Sequence...\n")

    n_start = int(input("please type here the number that you want to calculate: \n"))
    result = fibonacci_sequence(n_start)

    if isinstance(result, str):
        print(result)
    else:
        print("Fibonacci sequence : ", ", ".join(map(str, result)))


'''
    Utilizes:
    - isinstance(result, str): To check if the result from fibonacci_sequence() is an error message.
    - ", ".join(map(str, result)): To convert the list of Fibonacci numbers into a comma-separated string.
'''


if __name__ == "__main__":
    main_fib()


'''
Write a Python program that takes a positive integer N as input and prints
 the first N numbers of the Fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum
 of the two preceding ones, starting from 0 and 1.

For example, if the input is 6, the program should print: 0, 1, 1, 2, 3, 5.
'''