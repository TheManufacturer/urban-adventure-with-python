import random
import string


def generation_simply_password(length_password):
    password = ''.join(random.choice('0123456789') for _ in range(length_password))
    return password


def generation_complex_password(length_password):
    characters = (string.ascii_letters + string.digits +
                  string.punctuation)
    password = ''.join(random.choice(characters) for _ in range(length_password))
    return password


def main_gen_pass():
    print("Hello user, here we can create a random password")
    print("1. Create a simply random password")
    print("2. Create a simply random password")

    selection = input("Type a number for select modality generation :O ")

    length_password = int(input("Ok, now --> type length password -We  recommend 8 min length ;) "))

    if selection == '1':
        print("Random Simpy Password : ", generation_simply_password(length_password))
    elif selection == '2':
        print("Random password more difficult to find --> ", generation_complex_password(length_password))
    else:
        print("Strange...why u are here :( ")


if __name__ == "__main__":
    main_gen_pass()
