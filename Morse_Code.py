def morse2text(code, text):
    for i in code:
        if i == '.-':
            text.append('A')
        elif i == '-...':
            text.append('B')
        elif i == '-.-.':
            text.append('C')
        elif i == '-..':
            text.append('D')
        elif i == '.':
            text.append('E')
        elif i == '..-.':
            text.append('F')
        elif i == '--.':
            text.append('G')
        elif i == '....':
            text.append('H')
        elif i == '..':
            text.append('I')
        elif i == '.---':
            text.append('J')
        elif i == '-.-':
            text.append('K')
        elif i == '.-..':
            text.append('L')
        elif i == '--':
            text.append('M')
        elif i == '-.':
            text.append('N')
        elif i == '---':
            text.append('O')
        elif i == '.--.':
            text.append('P')
        elif i == '--.-':
            text.append('Q')
        elif i == '.-.':
            text.append('R')
        elif i == '...':
            text.append('S')
        elif i == '-':
            text.append('T')
        elif i == '..-':
            text.append('U')
        elif i == '...-':
            text.append('V')
        elif i == '.--':
            text.append('W')
        elif i == '-..-':
            text.append('X')
        elif i == '-.--':
            text.append('Y')
        elif i == '--..':
            text.append('Z')
    sol = ' '.join(text)
    return sol



def text2morse(code, morse):
    for i in code:
        if i == 'A':
            morse.append('.-')
        elif i == 'B':
            morse.append('-...')
        elif i == 'C':
            morse.append('-.-.')
        elif i == 'D':
            morse.append('-..')
        elif i == 'E':
            morse.append('.')
        elif i == 'F':
            morse.append('..-.')
        elif i == 'G':
            morse.append('--.')
        elif i == 'H':
            morse.append('....')
        elif i == 'I':
            morse.append('..')
        elif i == 'J':
            morse.append('.---')
        elif i == 'K':
            morse.append('-.-')
        elif i == 'L':
            morse.append('.-..')
        elif i == 'M':
            morse.append('--')
        elif i == 'N':
            morse.append('-.')
        elif i == 'O':
            morse.append('---')
        elif i == 'P':
            morse.append('.--.')
        elif i == 'Q':
            morse.append('--.-')
        elif i == 'R':
            morse.append('.-.')
        elif i == 'S':
            morse.append('...')
        elif i == 'T':
            morse.append('-')
        elif i == 'U':
            morse.append('..-')
        elif i == 'V':
            morse.append('...-')
        elif i == 'W':
            morse.append('.--')
        elif i == 'X':
            morse.append('-..-')
        elif i == 'Y':
            morse.append('-.--')
        elif i == 'Z':
            morse.append('--..')
        elif i == ' ':
            morse.append(' ')
#    return morse
    sol = ' / '.join(morse) + ' / '
    return sol


# Main Program
lis = []
print('Welcome to the Morse Code Translator.')
inputs = input('Enter a text message to translate to morse code, each letter seperated by /: ')
inputted = [i for i in inputs.split('/')]
print(inputs + ' in regular text is the letter/word ' + str(text2morse(inputted, lis)))