import sqlite3
from db_related import create_table, new_contact, all_contacts, update_contact, delete_contact


def switch_case(option):
    switcher = {
        '1': all_contacts,
        '2': new_contact,
        '3': update_contact,
        '4': delete_contact,
        '5': exit_program,
    }

    try:
        return switcher[option](cursor, database)
    except KeyError:
        return print("Invalid Option\n")


def exit_program(cursor, database):
    global program_running
    program_running = False


# create database
database = sqlite3.connect('D:\Development\My projects\python-projects-terminal\contact-book\contacts-book.db')
#
# # create cursor to create tables and manipulate data inside db
cursor = database.cursor()

# create contacts table on our db contacts-book
create_table(cursor)

program_running = True
while program_running:
    print(f"\n☎ Menu\n"
          f"{'-'*25}\n"
          "[1] See all contacts.\n"
          "[2] Add a new contact.\n"
          "[3] Update contact.\n"
          "[4] Delete contact.\n"
          "[5] Exit.")
    switch_case(input('Choose an option. '))

# close database
database.close()
