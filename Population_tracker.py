def pop_tracker() -> None:

    # Input validation for starting population
    while True:
        try:
            initial_population = float(
                input("What is the starting number of organisms?: ")
            )
            if initial_population <= 0:
                print("Starting population must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Input validation for daily increase percentage
    while True:
        try:
            daily_percent = float(
                input(
                    "What is the average daily population increase (as a percentage)?: "
                )
            )
            if daily_percent < 0:
                print("Daily increase cannot be negative.")
                continue
            pop_increase = daily_percent / 100
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Input validation for days
    while True:
        try:
            days = int(
                input(
                    "What is the number of days the organisms will be left to multiply?: "
                )
            )
            if days < 1:
                print("Number of days must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Day | Approximate Population")
    population = initial_population
    for day in range(1, days + 1):
        print(f"{day:3} | {population:>15.3f}")
        population *= 1 + pop_increase


pop_tracker()
