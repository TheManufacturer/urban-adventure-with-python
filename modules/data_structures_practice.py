def main_data_structures():
    close_program = False
    print("Hi my Freund : ;) \n")

    school_report_card = {
                        "Giuseppe Gullo": [("Matematica", 9, 0), ("Italiano", 7, 3), ("Inglese", 7.5, 4),
                                           ("Storia", 7.5, 4), ("Geografia", 5, 7)],
                        "Antonio Barbera": [("Matematica", 8, 1), ("Italiano", 6, 1),
                                            ("Inglese", 9.5, 0), ("Storia", 8, 2), ("Geografia", 8, 1)],
                        "Emiliano Ruozzo": [("Matematica", 7.5, 2), ("Italiano", 6, 2),
                                            ("Inglese", 4, 3), ("Storia", 8.5, 2), ("Geografia", 8, 2)]
                        }

    while not close_program:
        choose = int(input("U want see all the school report card ?         --> 1" 
                           "\n U want add your friend's Albert Einstein ;)     --> 2"
                           "\n U want add  Physics at all card                 --> 3"
                           "\n U want exit... ? :(                             --> 0\n"
                           ))

        if choose == 1:
            print(school_report_card, "\n")

        elif choose == 2:
            school_report_card["Albert Einstein"] = [("Matematica", 7.5, 2), ("Italiano", 6, 2), ("Inglese", 4, 3),
                                                     ("Storia", 8.5, 2), ("Geografia", 8, 2)]
            print(school_report_card)

        elif choose == 3:
            school_report_card["Giuseppe Gullo"].insert(0, ("Fisica", 9.5, 5))
            school_report_card["Antonio Barbera"].insert(1, ("Fisica", 8, 1))
            school_report_card["Emiliano Ruozzo"].insert(2, ("Fisica", 8, 3))
            school_report_card["Albert Einstein"].insert(3, ("Fisica", 10, 0))

        elif choose == 0:
            close_program = True

        #Todo Mancano i mini esercizi 4-5-6


if __name__ == "__main__":
    main_data_structures()


'''
Info Iniziali:

    - Giuseppe Gullo - Matematica (9/0) - Italiano (7/3) - Inglese (7.5/4) - Storia (7.5/4) - Geografia (5/7)
    - Antonio Barbera - Matematica (8/1) - Italiano (6/1) - Inglese (9.5/0) - Storia (8/2) - Geografia (8/1)
    - Emiliano Ruozzo - Matematica (7.5/2) - Italiano (6/2) - Inglese (4/3) - Storia (8.5/2) - Geografia (8/2)
    
Pagelle Scolastiche

Creare una struttura in grado di contenere record di diversi studenti.
La struttura sarà composta da un dizionario, con come chiavi il nome dello studente e come valore
una lista.

La lista deve conterene delle tuple, ogni tupla deve avere alla prima posizione il nome della materia, 
alla seconda il voto ed alla terza le ore di assenza.

1. Popola la struttura con i dati in tabella (*in fondo)

2. Aggiungi alla struttura dati la pagella di un nuovo studente chiamato Albert Enstein, con 10 in tutte le materie
    e nessuna ora di assenza.
    
3. Aggiungi Fisica a tutte le pagelle con le seguenti votazioni/assenze:
    
    - Giuseppe Gullo 9.5/0
    - Antonio Barbera 8/1
    - Emiliano Ruozzo 8/3
    - Albert Einstein 10/0

4. Stampa la tupla con le informazioni sulla materia Matematica per Giuseppe Gullo

5. Stampa la tupla con le informazioni sulla materia inglese per Emiliano Ruozzo

6. Stampa solo il voto di Antonio Barbera in Geografia


'''