import math
import binascii

def reverseString(string):
    reverse_string = ''
    for i in range(len(string)):
        reverse_string += string[len(string) - (i + 1)]
    return reverse_string


def numberToBinary(user_input):
    user_input = int(user_input)
    reverse_binary = ''
    while user_input >= 1:
        number = str(user_input % 2)
        user_input = math.floor(user_input / 2)
        reverse_binary += number

    def reverseString(string):
        reverse_string = ''
        for i in range(len(string)):
            reverse_string += string[len(string) - (i + 1)]
        return reverse_string

    binary = reverseString(reverse_binary)
    return binary


def binaryToNumber(user_input):
    user_input = str(user_input)
    for i in range(len(user_input)):
        if user_input[i] not in ['1', '0']:
            number = 'Invalid Input.'
            return number
    i = 0
    number = int(user_input[0])
    while i < len(user_input) - 1:
        number = (number * 2 + int(user_input[i + 1]))
        i += 1
    return number


def wordToBinary(user_input):
    binary = ' '.join(format(ord(i), 'b') for i in user_input)
    return binary


def binaryToWord(user_input):
    input_string = user_input.replace(' ', '')
    input_string = int(input_string, 2)

    total_bytes = (input_string.bit_length() + 7) // 8

    input_array = input_string.to_bytes(total_bytes, "big")

    ASCII_value = input_array.decode()
    return ASCII_value


def complementNumberToBinary(user_input):
    user_input = str(user_input)
    if user_input[0] == '-':
        user_input = user_input[1:]
        negative = True
    else:
        negative = False
    user_input = int(user_input)
    reverse_binary = ''
    while user_input >= 1:
        number = str(user_input % 2)
        user_input = math.floor(user_input / 2)
        reverse_binary += number

    original = reverseString(reverse_binary)
    length = 16 - len(original)
    padding = ''
    for i in range(length):
        padding += '0'
    new = padding + original
    complementstring = ''
    if negative == True:
        for i in range(len(new)):
            if new[15 - i] == '1':
                complementstring += '0'
            elif new[15 - i] == '0':
                complementstring += '1'
        binary = reverseString(complementstring)
        binary = bin(int(binary, 2) + int('00000000000000001', 2))
        binary = binary[2:]
    else:
        binary = new
    return binary


def check_bits(answer, bits):
    if len(answer) > bits:
        answer = f'Not enough bits. Needs {len(answer)} bits.'
    elif len(answer) < bits:
        needed = bits - len(answer)
        zero = ''
        for i in range(needed):
            zero += '0'
        answer = zero + answer
    return answer


def negative_state2_check_bits(answer, bits):
    if len(answer) >= bits:
        answer = f'Not enough bits. Needs {len(answer) + 1} bits.'
    elif len(answer) < bits:
        needed = bits - len(answer)
        zero = ''
        for i in range(needed - 1):
            zero += '0'
        answer = '1' + zero + answer
    return answer


def complementToNumber(user_input):
    for i in range(len(user_input)):
        if user_input[i] not in ['0', '1'] or len(user_input) != 16:
            answer = 'Invalid input.'
            return answer
    if user_input[0] == '0':
        i = 0
        while user_input[i] != '1':
            i += 1
        user_input = user_input[i:]
        return binaryToNumber(user_input)

    elif user_input[0] == '1':
        undo_complementstring = ''
        for i in range(len(user_input)):
            if user_input[15-i] == '1':
                undo_complementstring += '0'
            elif user_input[15-i] == '0':
                undo_complementstring += '1'
        print(undo_complementstring)
        answer = reverseString(undo_complementstring)
        i = 0
        while answer[i] != '1':
            i += 1
        answer = answer[i:]
        answer = int(binaryToNumber(answer)) + 1
        return '-' + str(answer)