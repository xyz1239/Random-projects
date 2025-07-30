class Car:
    SEDAN: int = 1
    COUPE: int = 2
    HATCHBACK: int = 3

    def __init__(
        self,
        bodyType: int = SEDAN,
        ccPower: int = 1000,
        color: str = "white",
        forSale: bool = False,
    ):
        self.__bodyType = bodyType
        self.__forSale = forSale
        self.__ccPower = ccPower
        self.__color = color

    def getBodyType(self) -> int:
        return self.__bodyType

    def setBodyType(self, bodyType: int) -> None:
        self.__bodyType = bodyType

    def isForSale(self) -> bool:
        return self.__forSale

    def setForSale(self, forSale: bool) -> None:
        self.__forSale = forSale

    def getCCPower(self) -> int:
        return self.__ccPower

    def setCCPower(self, ccPower: int) -> None:
        self.__ccPower = ccPower

    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str):
        self.__color = color


def main():

    car1 = Car(bodyType=Car.COUPE, ccPower=1800, color="white", forSale=True)
    car2 = Car(bodyType=Car.SEDAN, ccPower=2400, color="red", forSale=False)

    def get_body_type_name(body_type: int):
        if body_type == Car.SEDAN:
            return "SEDAN"
        elif body_type == Car.COUPE:
            return "COUPE"
        elif body_type == Car.HATCHBACK:
            return "HATCHBACK"
        else:
            return "Unknown"

    cars = [car1, car2]
    for idx, car in enumerate(cars, 1):
        body_type = get_body_type_name(car.getBodyType())
        color = car.getColor()
        cc_power = car.getCCPower()
        for_sale = "Yes" if car.isForSale() else "No"
        print(
            f"Car {idx}:\n"
            f"Body Type: {body_type}\n"
            f"Color: {color}\n"
            f"Engine Power (cc): {cc_power}\n"
            f"For Sale: {for_sale}\n"
        )


if __name__ == "__main__":
    main()
