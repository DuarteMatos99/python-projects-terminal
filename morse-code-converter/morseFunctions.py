from morseCode import MORSE_CODE_DICT


def convert_to_morse():
    user_input = input("Type something on text. ").strip()
    morse_code = ""
    message = user_input.upper()

    words = message.split(" ")
    for word in words:
        for char in word:
            if char in MORSE_CODE_DICT.keys():
                morse_code += f"{MORSE_CODE_DICT[char]} "
            else:
                return print("Cant contain weird symbols :(\n")
        morse_code = f"{morse_code} "
    return print(f"Output: {morse_code}\n")


def convert_to_text():
    user_input = input("Type something on morse code. ").strip()
    morse_code = ""

    words = user_input.split(" ")
    for word in words:
        if word in MORSE_CODE_DICT.values():
            morse_code += f"{list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(word)]}"
        elif word == '':
            morse_code = f"{morse_code} "
        else:
            return print("Cant contain weird symbols :(\n")

    return print(f"Output: {morse_code.capitalize()}\n")
