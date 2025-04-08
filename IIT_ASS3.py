def AAC():
    print("-" * 10)
    print("yabadabadoo")
    print("-" * 10)


def CSA():
    print("option 2")


def SMC():
    print("option 3")


def main():
    while True:
        print("=" * 25)
        print("Select an option: ")
        print("1. Problem 1: Automobile Alarm Circuit")
        print("2. Problem 2: Car Seatbelt Alarm System")
        print("3. Problem 3: Syrup Manufacturing Control")
        print("0. Exit")
        print("=" * 25)
        choice = input("Choose a problem: ").strip()

        if choice == "1":
            AAC()

        elif choice == "2":
            CSA()

        elif choice == "3":
            SMC()

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print(
                "Invalid option. Try again using numbers on the left side of the options. "
            )


if __name__ == "__main__":
    main()
