def pop_tracker() -> None:
    # inputs
    initial_population: float = float(
        input("What is the starting number of organisms?: ")
    )
    pop_increase: float = (
        float(
            input("What is the average daily population increase (as a percentage)?: ")
        )
        / 100
    )
    days: int = int(
        input("What is the number of days the organisms will be left to multiply?: ")
    )

    # maths
    population = initial_population * (1 + pop_increase) ** (days)

    print("Day | Approximate Population")
    population = initial_population
    for day in range(1, days + 1):
        print(f"{day:3} | {population:>15.3f}")
        population *= 1 + pop_increase


pop_tracker()
