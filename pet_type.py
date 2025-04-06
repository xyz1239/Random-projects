from typing import Dict


def register_pet(pets: Dict[str, str]):
    while True:
        name = input("Enter the new pet's name: ").strip()
        if not name:
            print("Pet name cannot be empty.")
            continue
        if name in pets:
            print(f"Oops! You already have a pet named {name}. Try another name.")
        else:
            pets[name] = "Unknown"
            print(f"{name} has been added to the database.")
            break


def main() -> None:
    pets: Dict[str, str] = {}  # Database: {name: type}

    while True:
        print("=" * 25)
        print("Enter your choice:")
        print("1. Register a Pet")
        print("2. Input Pet Animal Type")
        print("3. List All Pets")
        print("0. Quit")
        print("=" * 25)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_pet(pets)

        elif choice == "2":
            if not pets:  # Check if database is empty FIRST
                print("The database is empty. Please register a pet first.")
                continue  # Skip to main menu

            # Update Animal Type
            while True:
                name = input("Enter the pet's name: ").strip()
                if not name:
                    print("Pet name cannot be empty.")
                    continue
                if name not in pets:
                    print(
                        f"Huh? We don't have a {name} in our database. Try a registered name!"
                    )
                    break  # Exit loop to menu
                animal_type = input(
                    f"Enter {name}'s animal type (e.g., Dog, Cat): "
                ).strip()
                if not animal_type:
                    print("Animal type cannot be empty.")
                    continue
                pets[name] = animal_type
                print(f"{name}'s type has been updated to {animal_type}.")

                break

        elif choice == "3":
            # List All Pets
            if not pets:
                print("No pets in the database.")
            else:
                print("Pet Records:")
                for idx, (name, animal_type) in enumerate(pets.items(), 1):
                    print(f"{idx}. {name} ({animal_type})")

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
