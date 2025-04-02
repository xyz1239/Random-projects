from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class DietRestrictions:
    vegetarian: bool
    vegan: bool
    glutenfree: bool

    def match(self, required: DietRestrictions) -> bool:
        if required.veg and not self.vegetarian:
            return False
        if required.vegan and not self.vegan:
            return False
        if required.glutenfree and not self.glutenfree:
            return False
        return True

@dataclass
class Restaurant:
    name: str
    diet: DietRestrictions

RR = [Restaurant("joe's pizza", DietRestrictions(False, False, False))]
[Restaurant("Main Street Pizza Company", DietRestrictions(True, False, True))]
[Restaurant("Corner Café", DietRestrictions(True, True, True))]
[Restaurant("Mama’s Fine Italian", DietRestrictions(True, False, False))]
[Restaurant("The Chef’s Kitchen", DietRestrictions(True, True, True))]

#RESTAURANTS: List[Tuple[str, bool,bool,bool]]= [
("joe's pizza", False, False, False)
("Main Street Pizza Company", True, False, True)
("Corner Café", True, True, True)
("Mama’s Fine Italian", True, False, False)
("The Chef’s Kitchen", True, True, True)
#]


def ask_yn(prompt:str) -> bool:
    while True:
        response: str = input(prompt)
        if response.lower() in ("y", "yes"):
            return True
        if response.lower() in ("n", "no"):
            return False
        print("not a yes or no, please try again")

#def can_eat_at(r: Tuple[str, bool,bool,bool], veg, vegan, glu: bool)-> bool:
    if not veg or veg != r[1]:
        return False
    return True

def diet_inputs():
    vegetarian: bool = ask_yn("Is anyone in you party vegetarian?: ")
    vegan=bool(input("Is anyone in you party vegan?: "))
    glutenfree=bool(input("Is anyone in you party glutenfree?: "))

    required = DietRestrictions(vegetarian, vegan, glutenfree)
    for r in RR:
        if r.diet.match(required):
            print(r.name)

    #for r in RESTAURANTS:
        #if can_eat_at(r,vegetarian, vegan, glutenfree):
            print(r[0])



diet_inputs()