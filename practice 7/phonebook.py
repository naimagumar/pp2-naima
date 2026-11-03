
import csv
from connect import connect


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
        (name, phone)
    )

    conn.commit()
    print("Contact added!")

    cur.close()
    conn.close()


def show_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()

    for contact in contacts:
        print(contact)

    cur.close()
    conn.close()


def search_name():
    name = input("Enter name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE first_name ILIKE %s",
        ("%" + name + "%",)
    )

    contacts = cur.fetchall()

    for contact in contacts:
        print(contact)

    cur.close()
    conn.close()


def search_phone():
    phone = input("Enter phone prefix: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM contacts WHERE phone LIKE %s",
        (phone + "%",)
    )

    contacts = cur.fetchall()

    for contact in contacts:
        print(contact)

    cur.close()
    conn.close()


def update_name():
    phone = input("Enter phone: ")
    new_name = input("Enter new name: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET first_name = %s WHERE phone = %s",
        (new_name, phone)
    )

    conn.commit()
    print("Name updated!")

    cur.close()
    conn.close()


def update_phone():
    name = input("Enter name: ")
    new_phone = input("Enter new phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contacts SET phone = %s WHERE first_name = %s",
        (new_phone, name)
    )

    conn.commit()
    print("Phone updated!")

    cur.close()
    conn.close()


def delete_name():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE first_name = %s",
        (name,)
    )

    conn.commit()
    print("Contact deleted!")

    cur.close()
    conn.close()


def delete_phone():
    phone = input("Enter phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM contacts WHERE phone = %s",
        (phone,)
    )

    conn.commit()
    print("Contact deleted!")

    cur.close()
    conn.close()


def import_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                (row["first_name"], row["phone"])
            )

    conn.commit()
    print("CSV imported!")

    cur.close()
    conn.close()


while True:
    print("\nPHONEBOOK")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search by name")
    print("4. Search by phone prefix")
    print("5. Update name")
    print("6. Update phone")
    print("7. Delete by name")
    print("8. Delete by phone")
    print("9. Import CSV")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_name()
    elif choice == "4":
        search_phone()
    elif choice == "5":
        update_name()
    elif choice == "6":
        update_phone()
    elif choice == "7":
        delete_name()
    elif choice == "8":
        delete_phone()
    elif choice == "9":
        import_csv()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
