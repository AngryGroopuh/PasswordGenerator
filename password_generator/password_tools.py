import string
import secrets

def generate_pw(length, numbers=True, special_characters='', required_specials=''):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    characters = lowercase + uppercase

    pwd = [
        secrets.choice(lowercase),
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(uppercase),
    ]

    if numbers:
        characters += digits
        pwd.append(secrets.choice(digits))
        pwd.append(secrets.choice(digits))

    if special_characters:
        if required_specials != '':
            for char in required_specials:
                pwd.append(char)
                characters += char
        else:        
            characters += special_characters
            pwd.append(secrets.choice(special_characters))
            pwd.append(secrets.choice(special_characters))

    while len(pwd) < length:
        pwd.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(pwd)

    return ''.join(pwd)

def criteria_counts(password):
    char_counts = {'Uppercase':0, 'Lowercase':0, 'Numbers':0, 'Specials':0}

    for char in password:
        if char in string.ascii_uppercase:
            char_counts['Uppercase'] += 1
        elif char in string.ascii_lowercase:
            char_counts['Lowercase'] += 1
        elif char in string.digits:
            char_counts['Numbers'] += 1
        elif char in string.punctuation or char == ' ':
            char_counts['Specials'] += 1

    return char_counts

def validate_specials(special_input):
    valid_specials = ""
    invalid_specials = ""

    if special_input.lower() == "none":
        return True, "", ""

    if special_input == "":
        return True, string.punctuation, ""

    for character in special_input:
        if character not in valid_specials:
            if character == " ":
                valid_specials += character
            elif character not in string.punctuation:
                invalid_specials += character
            else:
                valid_specials += character

    if invalid_specials:
        return False, "", ""

    return True, valid_specials, valid_specials



