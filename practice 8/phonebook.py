
from connect import connect
def search_contacts():
    pattern = input("Enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()

    print("Contact added or updated!")

    cur.close()
    conn.close()


def bulk_insert_contacts():
    names = input("Enter names separated by commas: ").split(",")
    phones = input("Enter phones separated by commas: ").split(",")

    names = [x.strip() for x in names]
    phones = [x.strip() for x in phones]

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL bulk_insert_contacts(%s, %s, %s)",
        (names, phones, [])
    )

    invalid = cur.fetchone()[0]

    conn.commit()

    print("Invalid data:", invalid)

    cur.close()
    conn.close()


def show_contacts():
    limit = int(input("Contacts per page: "))
    page = int(input("Page number: "))

    offset = (page - 1) * limit

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def delete_contact():
    name = input("Enter name (or press Enter): ")
    phone = input("Enter phone (or press Enter): ")

    name = name if name else None
    phone = phone if phone else None

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL delete_contact(%s, %s)",
        (name, phone)
    )

    conn.commit()

    print("Contact deleted!")

    cur.close()
    conn.close()


while True:
    print("\nPHONEBOOK")
    print("1. Search contacts")
    print("2. Add or update contact")
    print("3. Add many contacts")
    print("4. Show contacts by pages")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        search_contacts()
    elif choice == "2":
        upsert_contact()
    elif choice == "3":
        bulk_insert_contacts()
    elif choice == "4":
        show_contacts()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")
