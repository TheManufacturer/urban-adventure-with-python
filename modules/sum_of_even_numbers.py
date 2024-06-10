def even_number_if_statement():
    somma: int = 0
    n = int(input("\n Please insert N for iter the cycle and find the even numbers : \n"))
    for i in range(1, n + 1):
        if i % 2 == 0:
            somma += i
    return somma


def even_number_while_statement():
    i = 0
    somma: int = 0
    n = int(input("\n Please insert N for iter the cycle and find the even numbers : \n"))
    while i < n:
        if i % 2 == 0:
            somma += i
        i += 1
    return somma


def main_even_number():
    close_program = False
    while not close_program:
        print("\n Here We have 2 methods for find a even number : \n")
        print("1. IF Statement : \n")
        print("2. WHILE Statement : ")
        print("\n ___Insert Y/N if u want use or not this program___")

        choose = input("\n Please insert here a number for ")

        if choose == '1':
            print("Sum of even numbers --> ", even_number_if_statement(), "\n")

        elif choose == '2':
            print("Sum of even numbers --> ", even_number_while_statement(), "\n")

        elif choose == "n":
            close_program = True
            print("Exiting the program ... :(")
            break

    print("Program exited")


if __name__ == "__main__":
    main_even_number()

'''
1. Leggi un numero intero N dall'utente.

2. Inizializza una variabile somma a 0.

3. Utilizza un ciclo per generare i primi N numeri pari.
    - In ogni iterazione del ciclo, aggiungi il numero pari corrente alla variabile somma.
    
4. Stampa la somma dei numeri pari.
'''
