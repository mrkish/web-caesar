def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)


def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated

def encrypt(text, key):
    message = ''
    index = 0

    # iterates through message
    for character in text:
        # filters alphas for floppydoodling
        if character.isalpha():
            # if index for keyword is longer
            # than keyword, reset to starting index
            if index > len(key) - 1:
                index = 0
                # gets alpha of key letter
                keylet = alphabet_position(key[(index)])
            else:  # cycles through rest of keyword
                keylet = alphabet_position(key[index])
            # key letter value passed as rot value to next func.
            message = message + rotate_character(character, keylet)
            # steps index value for next cycle
            index += 1
        else:
            # not alpha. not my problem.
            message = message + character
    # returns the allsparking secret
    return message

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]


def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char


    return rotated
