from typing import List, Tuple

@dataclass
class DietRestrictions:
    veg: bool
    vegan: bool
    gluten: bool

    def match(self, required: DietRestrictions) -> bool:
        if required.veg and not self.veg:
            return False
        
        return True

@dataclass
class Restaurant:
    name: str
    diet: DietRestrictions

RR = [Restaurant("foo", DietRestrictions(True, False, True))]

I_NAME, I_VEG, I_VEGAN, I_GLUTEN = range(4)

RESTAURANTS: List[Tuple[str, bool,bool,bool]]= [
("joe", False, False, False)
]


def ask_yn(prompt:str) -> bool:
    while True:
        response: str = input(prompt)
        if response.lower() in ("y", "yes"):
            return True
        if response.lower() in ("n", "no"):
            return False
        print("bad, try again")

def can_eat_at(r: Tuple[str, bool,bool,bool], veg, vegan, glu: bool)-> bool:
    if not veg or veg != r[1]:
        return False
    return True

def diet_inputs():
    vegetarian: bool = ask_yn("Is anyone in you party vegetarian?: ")
    vegan=bool(input("Is anyone in you party vegan?: "))
    glutenfree=bool(input("Is anyone in you party glutenfree?: "))

    required = DietRestrictions(veg, veg, glutenfree)
    for r in RR:
        if r.diet.match(required):
            printf(r.name)

    for r in RESTAURANTS:
        if can_eat_at(r,vegetarian, vegan, glutenfree):
            print(r[0])






diet_inputs()