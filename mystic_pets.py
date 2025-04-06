from typing import Dict, Any


def main() -> None:

    # Database: {normalized_name: {"name": str, "type": str, "parents": list, "children": list}}
    pets: Dict[str, Dict[str, Any]] = {}

    while True:
        print("=" * 25)
        print("1. Register a Pet")
        print("2. Update Pet Type")
        print("3. List All Pets")
        print("4. Define Parent-Child Relationship")
        print("5. Show Pet's Family")
        print("0. Quit")
        print("=" * 25)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            # Register Pet (with case normalization)
            while True:
                name = input("Enter the new pet's name: ").strip()
                if not name:
                    print("Pet name cannot be empty.")
                    continue
                normalized = name.lower()
                if normalized in pets:
                    print(f"Oops. A pet named {name} already exists.")
                    continue
                pets[normalized] = {
                    "name": name,
                    "type": "Unknown",
                    "parents": [],
                    "children": [],
                }
                print(f"{name} has been added to the database.")
                break

        elif choice == "2":
            # Update Animal Type (case-insensitive lookup)
            if not pets:
                print("The database is empty. Please register a pet first.")
                continue
            name = input("Enter pet's name: ").strip()
            normalized = name.lower()
            if normalized not in pets:
                print(f"{name} not found.")
                continue
            new_type = input(f"Enter {name}'s animal type (e.g., Dog, Cat): ").strip()
            if not new_type:
                print("Type cannot be empty.")
                continue
            pets[normalized]["type"] = new_type
            print(f"{name}'s type updated to {new_type}.")

        elif choice == "3":
            # List All Pets (preserve original casing)
            if not pets:
                print("No pets in the database.")
                continue
            print("Pet Records:")
            for idx, data in enumerate(pets.values(), 1):
                print(f"{idx}. {data['name']} ({data['type']})")

        elif choice == "4":
            # Define Parent-Child Relationship (case-insensitive + self-check)
            if not pets:
                print(
                    "Not enough pets to define a parent-child relationship. Please register more pets."
                )
                continue

            parent = input("Enter parent's name: ").strip()
            child = input("Enter child's name: ").strip()
            p_norm = parent.lower()
            c_norm = child.lower()

            # Validate existence
            if p_norm not in pets or c_norm not in pets:
                print("Both pets must be registered in the database.")
                continue

            # Validate self parenting
            if p_norm == c_norm:
                print("A pet cannot be its own parent.")
                continue

            # Validate animal type
            if pets[p_norm]["type"] != pets[c_norm]["type"]:
                parent_name: str = pets[p_norm]["name"]
                child_name: str = pets[c_norm]["name"]
                print(
                    f"Parent ({parent_name}) and child({child_name}) must be of the same animal type."
                )
                continue

            # Update relationships
            if c_norm not in pets[p_norm]["children"]:
                pets[p_norm]["children"].append(c_norm)
            if p_norm not in pets[c_norm]["parents"]:
                pets[c_norm]["parents"].append(p_norm)
            print(f"{parent} is now the parent of {child}.")

        elif choice == "5":
            # Show Pet's Family (case-insensitive lookup)
            if not pets:
                print("Database is empty. Please register a pet first.")
                continue
            name = input("Enter pet's name: ").strip()
            normalized = name.lower()
            if normalized not in pets:
                print(f"{name} not found.")
                continue
            data = pets[normalized]
            print(f"Family for {data['name']}:")
            print("Parents:")
            if len(data["parents"]) > 0:
                print("\n".join([f"- {name}" for name in data["parents"]]))
            print("Children:")
            if len(data["children"]) > 0:
                print("\n".join([f"- {name}" for name in data["children"]]))

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
