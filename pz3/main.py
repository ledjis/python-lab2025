from database.db_setup import create_tables, insert_initial_event_types
from services.event_sources import add_event_source, get_event_sources
from services.event_types import add_event_type, get_event_types
from services.security_events import *
import time


def show_menu():
    print("\n=== Security Monitoring System ===")
    print("1. Додати джерело подій")
    print("2. Додати тип події")
    print("3. Додати подію безпеки")
    print("4. Показати Login Failed за 24 год")
    print("5. Виявити brute-force атаки")
    print("6. Критичні події за тиждень")
    print("7. Пошук за ключовим словом")
    print("0. Вихід")


def main():
    create_tables()
    insert_initial_event_types()

    while True:
        show_menu()
        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Назва джерела: ")
            loc = input("Локація/IP: ")
            type_ = input("Тип: ")
            add_event_source(name, loc, type_)
            print("Джерело додано.")

        elif choice == "2":
            print("\nІснуючі типи подій:")
            for t in get_event_types():
                print(f"{t[0]}: {t[1]} [{t[2]}]")

            name = input("Тип події: ")
            sev = input("Серйозність: ")
            add_event_type(name, sev)
            print("Тип події додано.")

        elif choice == "3":
            print("\nДоступні джерела:")
            for s in get_event_sources():
                print(f"{s[0]}: {s[1]} ({s[2]})")

            s_id = int(input("ID джерела: "))

            print("\nДоступні типи подій:")
            for t in get_event_types():
                print(f"{t[0]}: {t[1]} [{t[2]}]")

            e_id = int(input("ID типу події: "))

            msg = input("Повідомлення: ")
            ip = input("IP (Enter якщо нема): ") or None
            user = input("Користувач (Enter якщо нема): ") or None

            add_security_event(s_id, e_id, msg, ip, user)
            print("Подію додано.")

        elif choice == "4":
            print(get_login_failed_last_24h())

        elif choice == "5":
            print(detect_bruteforce())

        elif choice == "6":
            print(get_critical_last_week())

        elif choice == "7":
            kw = input("Ключове слово: ")
            print(search_events(kw))

        elif choice == "0":
            break

        time.sleep(1)

if __name__ == "__main__":
    main()
