from database import *

create_database()

while True:
    print("\n1 - Add user")
    print("2 - Update password")
    print("3 - Authenticate user")
    print("4 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        login = input("Enter user name: ")
        password = input("Enter password: ")
        full_name = input("Enter full name: ")
        add_user(login, password, full_name)

    elif choice == "2":
        login = input("Enter login: ")
        new_password = input("Enter new password: ")
        update_password(login, new_password)

    elif choice == "3":
        login = input("Enter login: ")
        password = input("Enter password: ")
        authenticate_user(login, password)

    elif choice == "4":
        break

    else:
        print("Invalid option.")
