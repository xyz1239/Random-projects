from dataclasses import dataclass


#  Add Diet class
@dataclass
class DietRestrictions:
    vegetarian: bool
    vegan: bool
    glutenfree: bool

    def match(self, required: "DietRestrictions") -> bool:
        if required.vegetarian and not self.vegetarian:
            return False
        if required.vegan and not self.vegan:
            return False
        if required.glutenfree and not self.glutenfree:
            return False
        return True


# Add restarant class
@dataclass
class Restaurant:
    name: str
    diet: DietRestrictions


# List of Restaurants and Diets
RR = [
    Restaurant("joe's pizza", DietRestrictions(False, False, False)),
    Restaurant("Main Street Pizza Company", DietRestrictions(True, False, True)),
    Restaurant("Corner Café", DietRestrictions(True, True, True)),
    Restaurant("Mama’s Fine Italian", DietRestrictions(True, False, False)),
    Restaurant("The Chef’s Kitchen", DietRestrictions(True, True, True)),
]


# Prompt validation
def ask_yn(prompt: str) -> bool:
    while True:
        response: str = input(prompt)
        if response.lower() in ("y", "yes"):
            return True
        if response.lower() in ("n", "no"):
            return False
        print("not a yes or no, please try again")


# Diet inputs
def diet_inputs() -> None:
    vegetarian: bool = ask_yn("Is anyone in you party vegetarian?: ")
    vegan: bool = ask_yn("Is anyone in you party vegan?: ")
    glutenfree: bool = ask_yn("Is anyone in you party glutenfree?: ")

    required = DietRestrictions(vegetarian, vegan, glutenfree)
    for r in RR:
        if r.diet.match(required):
            print(r.name)


diet_inputs()
