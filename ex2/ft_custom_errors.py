class GardenError(Exception):
    pass


class PlantError(GardenError):

    def __str__(self) -> str:
        return "The tomato plant is wilting!"


class WaterError(GardenError):

    def __str__(self) -> str:
        return ("Not enough water in the tank!")


def test_errors() -> None:

    for error in GardenError.__subclasses__():
        print(f"Testing {error.__name__}...")
        try:
            raise error
        except error as e:
            print(f"Caught {error.__name__}: {e}\n")
    print("Testing catching all garden errors...")
    for error in GardenError.__subclasses__():
        try:
            raise error
        except GardenError as e:
            print(f"Caught a garden error: {e}")


if (__name__ == "__main__"):
    print("=== Custom Garden Errors Demo ===\n")
    test_errors()
    print("\nAll custom error types work correctly!")
