from password_manager.vault import (
    add_entry,
    list_entries,
    get_entry,
    delete_entry,
    generate_and_add,
    EntryNotFoundError,
)
from password_manager.generator import check_strength


def main() -> None:
    while True:
        print("\nPassword Manager")
        print("1. Generate and save password")
        print("2. Add password manually")
        print("3. List all services")
        print("4. Get password for service")
        print("5. Delete entry")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                service = input("Service name: ").strip()
                username = input("Username: ").strip()
                length_str = input("Password length [16]: ").strip()
                length = int(length_str) if length_str else 16
                password = generate_and_add(service, username, length)
                strength = check_strength(password)
                print(f"Generated password: {password}")
                print(f"Strength: {strength}")

            elif choice == "2":
                service = input("Service name: ").strip()
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                add_entry(service, username, password)
                strength = check_strength(password)
                print(f"Saved\n Strength: {strength}")

            elif choice == "3":
                entries = list_entries()
                for i, e in enumerate(entries, start=1):
                    print(
                        f"{i}. {e.service} ({e.username}) — created {e.created_at[:10]}"
                    )

            elif choice == "4":
                service = input("Service name: ").strip()
                entry = get_entry(service)
                print(f"Username: {entry.username}")
                print(f"Password: {entry.password}")

            elif choice == "5":
                service = input("Service name: ").strip()
                delete_entry(service)
                print(f"Deleted entry for {service}")

            elif choice == "6":
                print("Goodbye")
                break

            else:
                print("Invalid option")

        except EntryNotFoundError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()