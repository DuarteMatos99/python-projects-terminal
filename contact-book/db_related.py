def create_table(cursor):
    # create contacts table with fields. Just creating model for being created on db next with cursor
    sql_create_contacts_table = """ CREATE TABLE IF NOT EXISTS contacts(
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        phone_number NOT NULL
                                    );
                                """

    # create table on db with a cursor
    cursor.execute(sql_create_contacts_table)


def all_contacts(cursor, database):
    print("\n[*] Seeing all contacts [*]")
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    for row in rows:
        print(f"[{row[0]}] {row[1]}, {row[2]}")


def new_contact(cursor, database):
    print("\n[*] Adding a new contact [*]")
    contact_name = input("Contact name: ").capitalize().strip()
    if contact_name == '':
        return print('Contact name cannot be empty.')

    try:
        contact_phone = int(input("Contact phone: "))
    except ValueError:
        return print('Phone number cannot be empty or contain text.')

    contact = (contact_name, contact_phone)
    sql_new_contact = """ INSERT INTO contacts(name, phone_number) VALUES(?,?) """
    cursor.execute(sql_new_contact, contact)
    database.commit()
    print('Added new contact with success.')


def select_contact(cursor):
    contact_name = input("Contact name: ").strip().capitalize()
    if contact_name == '':
        return print('Contact name cannot be empty.')

    cursor.execute("SELECT * FROM contacts WHERE name=?", (contact_name,))
    rows = cursor.fetchall()
    if not rows:
        return print('Nothing found with that name.')

    new_rows = [{'id': row[0], 'name': row[1], 'phone_number': row[2]} for row in rows]
    for row in new_rows:
        print(f"[{row['id']}] {row['name']}, {row['phone_number']}")

    return new_rows


def update_contact(cursor, database):
    print("\n[*] Updating a contact [*]")
    new_rows = select_contact(cursor)
    option = input('Choose an option. ')
    try:
        contact = [row for row in new_rows if row['id'] == int(option)][0]
    except ValueError:
        return print("Invalid Option")
    else:
        if not contact:
            return print("No changes to contacts.")

        contact_name = input("New contact name: ").capitalize().strip()
        contact_phone = (input("New contact phone: "))
        if contact_name != '':
            contact['name'] = contact_name
        if contact_phone != '':
            contact['phone_number'] = contact_phone

        update_contact_database(contact, cursor, database)


def update_contact_database(contact, cursor, database):
    query = """UPDATE contacts SET name=?, phone_number=? WHERE id=?"""
    cursor.execute(query, (contact['name'], contact['phone_number'], contact['id']))
    database.commit()


def delete_contact(cursor, database):
    print("\n[*] Deleting a contact [*]")
    new_rows = select_contact(cursor)
    option = input('Choose an option. ')
    try:
        contact = [row for row in new_rows if row['id'] == int(option)][0]
    except ValueError:
        return print("Invalid Option")
    else:
        if not contact:
            return print("No changes to contacts.")

        delete_contact_database(contact, cursor, database)


def delete_contact_database(contact, cursor, database):
    query = """DELETE FROM contacts WHERE id=?"""
    cursor.execute(query, (contact['id'],))
    database.commit()
