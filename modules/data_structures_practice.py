import pprint

# subject_for_tuple = 0 --> With first position in tuple we can found the subject and operate

# Like Demo DB xD--> but more simply, so wew can populate
school_report_card = {
    "Giuseppe Gullo": [("Mathematics", 9, 0), ("Italian", 7, 3), ("English", 7.5, 4),
                       ("History", 7.5, 4), ("Geography", 5, 7)],
    "Antonio Barbera": [("Mathematics", 8, 1), ("Italian", 6, 1),
                        ("English", 9.5, 0), ("History", 8, 2), ("Geography", 8, 1)],
    "Emiliano Ruozzo": [("Mathematics", 7.5, 2), ("Italian", 6, 2),
                        ("English", 4, 3), ("History", 8.5, 2), ("Geography", 8, 2)]
}


def detailed_research_for_student(student, subject):
    found = False

    if student in school_report_card:
        for subject_tuple in school_report_card[student]:
            if subject_tuple[0] == subject:
                print(f"Report card for {student} for {subject}: {subject_tuple}")
                found = True
                break
        if not found:
            print(f"The subject {subject} is not present in {student}'s report card.")

    else:
        print(f"The student {student} is not present in the report card.")


def add_new_students():
    new_students = input(f"Enter the name of the new students")
    school_subjects = ["Mathematics", "Italian", "English", "History", "Geography"]
    new_report = []

    for subject in school_subjects:
        grades = float(input(f"Enter the grade for {subject} for {new_students}:"))
        absences = int(input(f"Enter the absences for {subject} for {new_students}"))
        new_report.append((subject, grades, absences))

    school_report_card[new_students] = new_report


def add_new_subject():
    for student in school_report_card:
        school_subject = input(f"Enter the new school_subject for {student}: ")
        grade = float(input(f"Enter the grade for {school_subject}, for {student}: "))
        absences = int(input(f"Enter the number of absences for {school_subject}, for {student}: "))

        school_report_card[student].append((school_subject, grade, absences))


def main_data_structures():
    close_program = False
    print("Hi meine Freund : ;) \n")

    while not close_program:

        choose = int(input("U want see all the school report card ?                                 --> 1" 
                           "\n U want add add new student? ;)                                       --> 2"
                           "\n U want add  new school subject + report  at all card                 --> 3"
                           "\n In-depth research for student                                        --> 4"
                           "\n In-depth research for student (only grades for subject)              --> 5"
                           "\n U want exit... ? :(                                                  --> 0\n"

                           ))

        if choose == 1:
            pprint.pprint(school_report_card)

        elif choose == 2:
            add_new_students()
            pprint.pprint(school_report_card)

        elif choose == 3:
            add_new_subject()
            pprint.pprint(school_report_card)

        elif choose == 4:
            student = input("Inserisci il nome dello studente: ")
            subject = input("Inserisci la materia: ")
            
            detailed_research_for_student(student, subject)

        elif choose == 5:
            # Same like detailed_research_for_student(student, subject) but only grades for subject
            student = input("Inserisci il nome dello studente: ")
            subject = input("Inserisci la materia: ")
            found = False

            if student in school_report_card:
                for subject_tuple in school_report_card[student]:
                    if subject_tuple[0] == subject:
                        print(f"Report card for {student} for {subject}: {subject_tuple[1]}")
                        found = True
                        break
                if not found:
                    print(f"The subject {subject} is not present in {student}'s report card.")

            else:
                print(f"The student {student} is not present in the report card.")

        elif choose == 0:
            close_program = True


if __name__ == "__main__":
    main_data_structures()


'''

Info Iniziali:

    - Giuseppe Gullo - Mathematics (9/0) - Italian (7/3) - English (7.5/4) - History (7.5/4) - Geography (5/7)
    - Antonio Barbera - Mathematics (8/1) - Italian (6/1) - English (9.5/0) - History (8/2) - Geography (8/1)
    - Emiliano Ruozzo - Mathematics (7.5/2) - Italian (6/2) - English (4/3) - History (8.5/2) - Geography (8/2)
    
-----

Pagelle Scolastiche

- Creare una struttura in grado di contenere record di diversi studenti.

- La struttura sarà composta da un dizionario, con come chiavi il nome dello studente e come valore
    una lista.

- La lista deve contenere delle tuple, ogni tupla deve avere alla prima posizione il nome della materia, 
    alla seconda il voto ed alla terza le ore di assenza.

----- 
1. Popola la struttura con i dati in tabella.

2. Aggiungi alla struttura dati la pagella di un nuovo studente chiamato Albert Einstein, con 10 in tutte le materie
    e nessuna ora di assenza.
    
3. Aggiungi Fisica a tutte le pagelle con le seguenti votazioni/assenze:
    
    - Giuseppe Gullo 9.5/0
    - Antonio Barbera 8/1
    - Emiliano Ruozzo 8/3
    - Albert Einstein 10/0

4. Stampa la tupla con le informazioni sulla materia Mathematics per Giuseppe Gullo

5. Stampa la tupla con le informazioni sulla materia English per Emiliano Ruozzo

6. Stampa solo il voto di Antonio Barbera in Geography


'''