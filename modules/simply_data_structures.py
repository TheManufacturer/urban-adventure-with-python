# Define a tuple with subject names
subjects = ("English", "Physics", "Geography", "Mathematics")

shopping_list = [
    "milk", "bread", "eggs", "cheese", "apples", "bananas", "chicken", "rice",
    "pasta", "tomatoes", "carrots", "potatoes", "yogurt", "butter", "orange juice",
    "lettuce", "onions", "garlic", "peppers", "cereal", "coffee", "tea", "sugar",
    "flour", "olive oil", "salt", "pepper", "spinach", "cucumbers", "mushrooms",
    "bacon", "ham", "sausages", "fish", "shrimp", "bread rolls", "chocolate",
    "ice cream", "cookies", "toilet paper", "paper towels", "dish soap", "laundry detergent"
]


def exercise_tuple_simply():
    print("In this method we have le max length of element in tupla")
    print(f"the subjects : {subjects}")

    # Initialize a variable to find the longest subject name
    max_length_subject = subjects[0]

    # Loop to find the longest subject name
    for subject in subjects:
        # Check if the current subject name is longer than the current max_length_subject
        if len(subject) > len(max_length_subject):
            max_length_subject = subject

    # Print the longest subject name found
    print(f"Subject with the longest name is: {max_length_subject}")


def exercise_tuple_index():
    print("Here we can have (index and value)of tupla   --> using enumerate function")

    # Use enumerate to get both index and value
    # [return for ex: ("English", 0) so, we can have index and value]
    for index, value in enumerate(subjects):
        print(f"Element : {value}, position n° {index} ")

# ToDo Exercise Simply Dictionary :)


def exercise_dictionary_simply():
    pass


def simply_data_exercise():
    exercise_tuple_index()
    print("\n")
    exercise_tuple_simply()


if __name__ == "__main__":
    simply_data_exercise()

'''
---Esercizio con le liste

    -Continue e Break (creare un esercizio) esempio:
        - Se presente un cibo in particolare o altro usare "break" in un <def> e "continue"
            in un altro così da capire la differenza --> Nella stampa includiamo anche *len()*


--- Esercizio sulle Tuple: (Accesso ed Informazioni)

- Descrizione: 
    Definisci una tupla contenente nomi di materie scolastiche. 
    Per ciascuna materia, stampa il nome e la lunghezza della parola più lunga.
    
    --> "English", "Physics", "Geography", "Mathematics"

- Obiettivo: 
    Esercitare l'accesso agli elementi di una tupla e l'utilizzo 
    del metodo len() per ottenere la lunghezza di una stringa.

-- Dettagli aggiuntivi: 
    
    Includi anche un esempio su come accedere agli elementi di una tupla 
    utilizzando indici numerici.

---Esercizio sui Dizionari: (Aggiornamento e Stampa)

- Descrizione: 
    Crea un dizionario iniziale con alcuni studenti e i loro voti in alcune materie. 
    Consentire all'utente di aggiornare i voti di uno studente e stampare il dizionario aggiornato.

- Obiettivo: 
    Esercitare l'aggiornamento di valori in un dizionario e la stampa del dizionario.

- Dettagli aggiuntivi: 
    Includi un esempio su come aggiungere uno studente al dizionario e 
    come stampare il dizionario completo dopo l'aggiornamento.
'''