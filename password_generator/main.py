import string
import secrets
import password_tools

def banner():
    print('\n\n')
    print('                  ~| PASSWORD GENERATOR |~')
    print('Defaults will generate a 8 character password including at least')
    print('2 uppercase, 2 lowercase, 2 numbers, and 2 special characters.\n')
    print('*If special characters are provided, the password will contain each ')
    print(' character at least once, and default characters will be ignored.\n')

def get_has_number():
    while True:  
        has_number = input('Include numbers? (Y/n): ').lower()  
        if has_number == '' or has_number == 'y':
            return True
        elif has_number == 'n':
            return False
        elif has_number not in ('y', 'n'):
            print('Invalid. Please enter "y", "n", or press enter for default.')

def get_specials():
    while True:
        valid_specials = ''
        invalid_specials = ''
        
        special_input = input('Special characters (Enter=default, none=off): ')

        if special_input.lower() == 'none':
            special_chars = ''
            break
        elif special_input == '':
            special_chars = string.punctuation
            break

        for character in special_input:
            if character not in valid_specials:
                if character == ' ':
                    valid_specials += character
                elif character not in string.punctuation:
                    invalid_specials += character      
                else:
                    valid_specials += character

        special_reqs = valid_specials != '' and invalid_specials == ''

        if special_reqs:
            special_chars = valid_specials
            break
        else:
            print('\nPlease only use valid special characters\n')
            print(f"Valid characters: {string.punctuation}")
            print(f"Invalid characters entered: {invalid_specials}\n")

    return valid_specials, special_chars

def get_pw_length(has_number, special_chars, valid_specials):
    while True:
        minimum_required = 4

        if has_number:
            minimum_required += 2

        if special_chars:
            if valid_specials == '':
                minimum_required += 2
            else:
                minimum_required += len(valid_specials)
                
        length = input(f"Password length ('Enter' for min. {minimum_required}): ")

        if length == '':
            length = minimum_required
            return length
        elif not length.isdigit():
            print('Must be digits')
        elif int(length) >= minimum_required:
            length = int(length)
            return length
        else:
            print(f"Password length must be at least {minimum_required}")


banner()
while True:
    
    has_number = get_has_number()

    valid_specials, special_chars = get_specials()

    length = get_pw_length(has_number, special_chars, valid_specials)

    pwd = password_tools.generate_pw(length, has_number, special_chars, valid_specials)
    print(f"\n\nPassword:\n{pwd}\n\n")

    char_counts = password_tools.criteria_counts(pwd)
    for char, count in char_counts.items():
        print(f"{char}: {count}")

    rerun = input('\n\nPress "Enter" to generate another password ("q" to quit): ')
    if rerun.lower() == 'q':
        break


