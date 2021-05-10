from morseCode import logo
from morseFunctions import convert_to_morse, convert_to_text
from time import sleep


def switch_case(option):
    switcher = {
        '1': convert_to_morse,
        '2': convert_to_text,
        '3': close_program,
    }

    try:
        return switcher[option]()
    except KeyError:
        return print("Invalid Option\n")


def close_program():
    global program_is_running
    program_is_running = False


program_is_running = True
print(logo, "\nWelcome to Morse Code converter.")

while program_is_running:
    print("*---------------------------------*\n"
          "[1] Convert to text to code morse\n"
          "[2] Convert to code morse to text\n"
          "[3] Exit\n"
          "*---------------------------------*")
    switch_case(input("Choose an option: "))
    sleep(1)
