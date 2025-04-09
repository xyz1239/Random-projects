def AAC():
    try:
        print("=" * 25)
        print("Problem 1: Automobile Alarm Circuit has been selected")
        door = int(
            input(
                "Is the driver door open or closed (answer 1 for open or 0 for closed): "
            )
        )
        ignition = int(
            input("Is the ignition on or off (answer 1 for on or 0 for off): ")
        )
        headlights = int(
            input("Are the headlights on or off (answer 1 for on or 0 for off): ")
        )
        print("=" * 25)
    except ValueError:
        print("Error: Please enter either a 0 or a 1")
        exit()

    if not all(val in {0, 1} for val in [door, ignition, headlights]):
        print("Error: Values must be 0 or 1.")
        exit()

    condition1 = headlights == 1 and ignition == 0
    condition2 = door == 1 and ignition == 1

    if condition1 or condition2:
        print("Alarm is on bzzt bzzt bzzt")
        if condition1:
            print("Headlight are on and Ignition is off causing alarm to trigger")
        if condition2:
            print("Door is open and the Ignition is on causing alarm to trigger")
    else:
        print("Alarm is not triggered")


def CSA():
    try:
        print("=" * 25)
        print("Problem 2: Car Seatbelt Alarm System has been selected")
        DRIV = int(input("Is the driver seat occupied? (answer 1 for yes or 0 for no)"))
        PASS = int(
            input("Is the passanger seat occupied? (answer 1 for yes or 0 for no)")
        )
        IGN = int(input("Is the igniton on? (answer 1 for yes or 0 for no)"))
        BELTD = int(
            input("Is the driver seatbelt fastened? (answer 1 for yes or 0 for no)")
        )
        BELTP = int(
            input("Is the passenger seatbelt fastened? (answer 1 for yes or 0 for no)")
        )
        print("=" * 25)
    except ValueError:
        print("Error: Please enter either a 0 or a 1")
        exit()

    if not all(val in {0, 1} for val in [DRIV, PASS, IGN, BELTD, BELTP]):
        print("Error: Values must be 0 or 1.")
        exit()

    condition_driver = IGN == 1 and DRIV == 1 and BELTD == 0
    condition_passenger = IGN == 1 and PASS == 1 and BELTP == 0

    if condition_driver or condition_passenger:
        print("Alarm is on bzzt bzzt bzzt")
        if condition_driver:
            print(
                "Alarm is triggered becasue the Ignition is on and the Driver is in the seat without a seatbelt"
            )
        if condition_passenger:
            print(
                "Alarm is triggered becasue the Ignition is on and the Passenger is in the seat without a seatbelt"
            )
    else:
        print("Alarm is not triggered")


def SMC():
    try:
        print("=" * 25)
        print("Problem 3: Syrup Manufacturing Control has been selected")
        L_max = int(input("Is the level at maximum? (answer 1 for yes or 0 for no)"))
        L_min = int(input("Is the level at minimum? (answer 1 for yes or 0 for no)"))
        F_inlet = int(input(""))
        Temp = int(input(""))
        print("=" * 25)
    except ValueError:
        print("Error: Please enter either a 0 or a 1")
        exit()

    if not all(val in {0, 1} for val in [L_max, L_min, F_inlet, Temp]):
        print("Error: Values must be 0 or 1.")
        exit()

    V_inlet = (L_max == 0 and F_inlet == 1) or (
        L_max == 0 and L_min == 0 and F_inlet == 0
    )
    V_outlet = L_min == 1 and F_inlet == 0 and Temp == 1

    if V_inlet or V_outlet:
        if V_inlet:
            print("Inlet is open.")
        if V_outlet:
            print("Outlet is open.")
    else:
        print("Nothing is open.")


def SMC_Logic():
    try:
        print("=" * 25)
        print("Problem 3: Syrup Manufacturing Control has been selected")
        L_max = int(input("Is the level at maximum? (answer 1 for yes or 0 for no)"))
        L_min = int(input("Is the level at minimum? (answer 1 for yes or 0 for no)"))
        F_inlet = int(input(""))
        Temp = int(input(""))
        print("=" * 25)
    except ValueError:
        print("Error: Please enter either a 0 or a 1")
        exit()

    if not all(val in {0, 1} for val in [L_max, L_min, F_inlet, Temp]):
        print("Error: Values must be 0 or 1.")
        exit()

    V_inlet = (
        (not L_max and not L_min and not F_inlet)
        or (not L_max and not L_min and F_inlet)
        or (not L_max and L_min and F_inlet)
    )
    V_outlet = (not L_max and L_min and not F_inlet and Temp) or (
        L_max and L_min and not F_inlet and Temp
    )

    if V_inlet or V_outlet:
        if V_inlet:
            print("Inlet is open.")
        if V_outlet:
            print("Outlet is open.")
    else:
        print("Nothing is open.")


def main():
    while True:
        print("=" * 25)
        print("Select an option: ")
        print("1. Problem 1: Automobile Alarm Circuit")
        print("2. Problem 2: Car Seatbelt Alarm System")
        print("3. Problem 3: Syrup Manufacturing Control (Truthtables)")
        print("4. Problem 3: Syrup Manufacturing Control (Logic)")
        print("0. Exit")
        print("=" * 25)
        choice = input("Choose a problem: ").strip()

        if choice == "1":
            AAC()

        elif choice == "2":
            CSA()

        elif choice == "3":
            SMC()

        elif choice == "4":
            SMC_Logic()

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break

        else:
            print(
                "Invalid option. Try again using numbers on the left side of the options. "
            )


if __name__ == "__main__":
    main()
