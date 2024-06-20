import re

list_of_emails = [
    # Email valide
    'johndoe@example.com',
    'alice_smith123@email.co.uk',
    'info@company.net',
    'jane_doe-123@example.com',
    'user123@example.org',

    # Email non valide
    'john.doe.example.com',           # manca il carattere '@'
    'john.doe@company',               # manca l'estensione del dominio
    'info@company.',                  # l'estensione del dominio è troppo breve
    'user123@company.longextension',  # l'estensione del dominio è troppo lunga
    '@example.com'                    # manca l'username
]


def using_regex_pattern(user_email):
    # Define a regex pattern for validating email addresses
    regex_pattern = r'^[\w.-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'

    # Explanation of the regex pattern:
    # ^               : Start of the string
    # [\w.-]+         : One or more word characters (letters, digits, underscores), dots, or hyphens
    # @               : Literal '@' character
    # [A-Za-z0-9]+    : One or more letters (uppercase or lowercase) or digits (domain part)
    # \.              : Literal '.' character (escaped because '.' is a special character in regex)
    # [A-Za-z]{1,3}   : One to three letters (uppercase or lowercase) (extension part)
    # $               : End of the string

    # Use the re.match function to check if the user_email matches the regex pattern
    if re.match(regex_pattern, user_email):
        print("Valid Email Address")
    else:
        print("Not Valid Email Address")


def validator_email(list_of_emails):
    pass


def validator_email_main():
    user_email = input("Write here your email --> : \n")
    using_regex_pattern(user_email)
    validator_email(list_of_emails)


if __name__ == "__main__":
    validator_email_main()


# email format --> username@domain.extension
# username contains only --> words/numbers/(-)/(_)/
# domain contains only --> words/number
# extension --> (max length = 3)

    # regex_pattern = r'^[\w.-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'

    # Spiegazione del pattern regex:
    # ^               : Inizio della stringa
    # [\w.-]+         : Una o più occorrenze di caratteri alfanumerici (lettere, cifre, underscore), punti o trattini
    # @               : Carattere '@' letterale
    # [A-Za-z0-9]+    : Una o più lettere (maiuscole o minuscole) o cifre (parte del dominio)
    # \.              : Carattere '.' letterale (con la barra rovesciata per indicare: un punto letterale
    # [A-Za-z]{1,3}   : Da una a tre lettere (maiuscole o minuscole) (parte dell'estensione)
    # $               : Fine della stringa
