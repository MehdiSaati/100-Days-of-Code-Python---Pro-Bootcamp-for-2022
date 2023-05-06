# Python program to implement Morse Code Translator

# dictionary for mapping characters to morse code
CHARS_TO_MORSE_CODE_MAPPING = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}
WELCOME_MESSAGE = '''
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    |M|o|r|s|e| |C|o|d|e| |E|n|c|o|d|e|r|
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+  
                 |MEHDI|
    +-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+
    '''

# function to encode plain English text to morse code
def morse_code_encrypt(english_plain_text):
    morse_code = ''
    for char in english_plain_text:
        # checking for space
        # to add single space after every character and double space after every word
        if char == ' ':
            morse_code += '  '
        else:
            # adding encoded morse code to the result
            morse_code += CHARS_TO_MORSE_CODE_MAPPING[char.upper()]
    return morse_code

# function to decode morse code to plain English text 
def to_english_plain_text(morse_code):
    MORSE_CODE_TO_CHARS_MAPPING = {v: k for k, v in CHARS_TO_MORSE_CODE_MAPPING.items()}

    english_plain_text = ''

    current_char_morse_code = ''
    i = 0
    while i < len(morse_code) - 1:
        
        # checking for each character
        if morse_code[i] == ' ':
            # checking for word
            if len(current_char_morse_code) == 0 and morse_code[i + 1] == ' ':
                english_plain_text += ' '
                i += 1
            else:
                # adding decoded character to the result
                english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
                    current_char_morse_code]
                current_char_morse_code = ''              

        else:
            # adding morse code char to the current character
            current_char_morse_code += morse_code[i]
        i += 1

    # adding last character to the result
    if len(current_char_morse_code) > 0:
        english_plain_text += MORSE_CODE_TO_CHARS_MAPPING[
            current_char_morse_code]
       
    return english_plain_text

# Hard-coded driver function to run the program
def main():
    
    print(WELCOME_MESSAGE)
    print('Welcome to Morse Code Encoder !! \n')
    english_plain_text = input('Please provide a String to convert? ')
    result = morse_code_encrypt(english_plain_text.upper())
    print (f'Morse Code : {result} \n')
    
    message = input('Please provide a Morse Code String to decrypt? ')
    english_plain_text = to_english_plain_text(message)
    print (f'English Text : {english_plain_text}')
 
# Executes the main function
if __name__ == '__main__':
    main()
