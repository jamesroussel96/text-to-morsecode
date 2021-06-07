# A-Z , 0-9, space
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

# A-Z , 0-9, space
international_morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
                            '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--',
                            '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....',
                            '-....', '--...', '---..', '----.', '/']

user_message = input('Please enter the message you would like translated to morse code\n').lower()


def character_index():
    characters = []
    for character in user_message:
        characters.append(english.index(character))
    return characters


index = (character_index())

print('This message translated to morse code is...\n')

for character in index:
    print(international_morse_code[character], end='')


