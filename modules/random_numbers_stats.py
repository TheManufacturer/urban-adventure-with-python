import random


def random_sequence_numbers(user_range):
    random_numbers = [random.randint(1, 100) for _ in range(user_range)]
    return random_numbers


def operation_with_random_numbers(random_numbers):
    total = sum(random_numbers)
    average = total / len(random_numbers)
    maximum = max(random_numbers)
    return total, average, maximum


def main_random_work():
    user_range = int(input("Please, type here range for operation --> Danke Brò \n"))
    random_number = random_sequence_numbers(user_range)
    total, average, maximum = operation_with_random_numbers(random_number)
    print("Sequence of Random Number : ", random_number)
    print("Sum of Random Number : ", total)
    print("Average of Random Number : ", average)
    print("Max Value : ", maximum)


if __name__ == "__main__":
    main_random_work()
