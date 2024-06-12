def sum_vector_element(vector):
    sum = 0
    vector_length: int = len(vector)
    for i in range(vector_length):
        sum += vector[i]
    return sum


def find_element(vector, number_to_find):
    count = 0
    for element in vector:
        if element == int(number_to_find):
            count += 1
    return count


def sort_vector(vector):
    n = len(vector)
    for i in range(n):
        for j in range(0, n-i-1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector


def create_vector():
    vector = []
    print("Hii...are u ready... ?\n")
    while True:
        element = input("please insert here elements for vector /oneForTime ;)\n")
        if element == '':
            break
        try:
            vector.append(int(element))
        except ValueError:
            print("Not valid integer...your array maybe are ready")
    return vector


def main_operation_vector():
    close_program = False
    print("Hello--> Here we work with vector")
    print("Firs of all, let's create the vector...\n")
    vector = create_vector()

    while not close_program:
        print("now we can operate with this vector", vector, "\n")

        choose = int(input("Now you can : "
                           "\n 1. sum vector's element "
                           "\n 2. find element in vector "
                           "\n 3. Sort vector "
                           "\n 0. write 0 and go away ... :( \n"))
        if choose == 1:
            print("The sum of vector : ", sum_vector_element(vector))

        elif choose == 2:
            (number_to_find) = input("Type here the word that u want find\n")
            print("Found number --> ", number_to_find, find_element(vector, number_to_find), "times")

        elif choose == 3:
            print(sort_vector(vector))

        else:
            "maybe you want exit ? :("
            close_program = True


if __name__ == "__main__":
    main_operation_vector()


'''
1. Sum vector elements

2. Find element in vector

3. Sort vector elements
'''