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


def main_operation_builtin_methods():
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
            print("The sum of vector : ", sum(vector))

        elif choose == 2:
            (number_to_find) = int(input("Type here the word that u want find\n"))
            print("Found number --> ", number_to_find, vector.count(number_to_find), "times")

        elif choose == 3:
            print(vector.sort())

        else:
            "maybe you want exit ? :("
            close_program = True


if __name__ == "__main__":
    main_operation_builtin_methods()


'''
List Methods:
1. append(element)
    - Adds an element to the end of the list.
    
2. extend(iterable) 
    - Extends the list by appending elements from the iterable.
    
3. insert(index, element) 
    - Inserts an element at the specified index.
    
4. remove(element) 
    - Removes the first occurrence of the specified element from the list.
    
5. pop([index]) 
    - Removes and returns the element at the specified index (default is the last element).
        
6. clear() 
    - Removes all elements from the list.
    
7. index(element[, start[, end]]) 
    - Returns the index of the first occurrence of the specified element in the list.
    
8. count(element) 
    - Returns the number of occurrences of the specified element in the list.
    
9. sort(key=None, reverse=False) 
    - Sorts the elements of the list in ascending order 
        (optional key and reverse parameters).
        
10. reverse() 
    - Reverses the order of the elements in the list.

11. copy() 
    - Returns a shallow copy of the list.

Built-in List Functions:
1. len(list) 
    - Returns the number of elements in the list.
    
2. sum(list) 
    - Returns the sum of all elements in the list (if numeric).
    
3. min(list) 
    - Returns the smallest element in the list.
    
4. max(list) 
    - Returns the largest element in the list.
    
5. sorted(list) 
    - Returns a new sorted list from the elements of the given iterable.

'''