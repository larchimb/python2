class GardenError():

    def __init__(self) -> None:
        for subclass in GardenError.__subclasses__():
            subclass()


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass

if (__name__ == "__main__"):
