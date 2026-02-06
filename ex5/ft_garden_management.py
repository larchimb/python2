class Plant():
    """Represents a plant with its characteristics."""
    def __init__(self, name: str, water: int, sun: int) -> None:
        """Initialize plant characteristics"""
        self.name = name
        self.water = water
        self.sun = sun

    def __str__(self) -> str:
        """Return all infos"""
        return (f"{self.name}: healthy (water: {self.water}, sun: {self.sun})")


class GardenError(Exception):
    pass


class PlantError(GardenError):

    def __str__(self) -> str:
        return "No plants in your garden!!"


class WaterError(GardenError):

    def __str__(self) -> str:
        return ("Not enough water in the tank!")


class GardenManager():
    """This class groups all method to manage a garden"""
    plant_list = []
    water_tank = 2
    issues = ""

    @staticmethod
    def add_many_plants(data: list[tuple[str, int, int]]) -> None:
        """Add many plants to a garden"""
        text = "Adding plants to garden...\n"
        for plant in data:
            name = plant[0] or None
            try:
                water = plant[1]
            except IndexError:
                water = None
            try:
                sun = plant[2]
            except IndexError:
                sun = None
            text += GardenManager.add_plant(name, water, sun)
        print(text)

    @classmethod
    def add_plant(cls, name: str | None,
                  water: int | None, sun: int | None) -> str:
        """Add one plant to a specific garden"""
        try:
            if (type(name) is not str or len(name) == 0):
                raise ValueError("Error: Plant name must be a string!\n")
            elif (type(water) is not int or water < 0):
                raise ValueError(f"Error: Water must be >= 0 for {name}!\n")
            elif (type(sun) is not int or sun < 0):
                raise ValueError(f"Error: Sun must be >= 0 for {name}!\n")
        except ValueError as e:
            return (f"{e}")
        cls.plant_list.append(Plant(name, water, sun))
        return (f"Added {name} successfully\n")

    @classmethod
    def water_plants(cls) -> None:
        try:
            print("Watering plants...\nOpening watering systems")
            for plant in cls.plant_list:
                if (cls.water_tank <= 0):
                    print(f"Watering {plant.name} - failure")
                    raise WaterError
                print(f"Watering {plant.name} - success")
                plant.water += 1
                cls.water_tank -= 1
            if (len(cls.plant_list) == 0):
                raise PlantError
        except GardenError as e:
            cls.issues += (f"Caught GardenError in water_plants: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    @classmethod
    def check_plant_health(cls):
        try:
            if (len(cls.plant_list) == 0):
                raise PlantError
        except GardenError as e:
            cls.issues += (f"Caught GardenError in plant_health: {e}")
        print("Checking plant health...")
        for plant in cls.plant_list:
            cls.check_health(plant)
        print()

    @staticmethod
    def check_health(plant: Plant):
        try:
            if (plant.water < 1):
                raise ValueError(f"Error: Water level {plant.water} is "
                                 "too low (min 1)")
            elif (plant.water > 10):
                raise ValueError(f"Error: Water level {plant.water} is "
                                 "too high (max 10)")
            elif (plant.sun < 2):
                raise ValueError("Error: Sunlight hours "
                                 f"{plant.sun} is too low (min 2)")
            elif (plant.sun > 12):
                raise ValueError("Error: Sunlight hours "
                                 f"{plant.sun} is too high (max 12)")
            else:
                print(f"Plant '{plant.name}' is healthy!")
        except (ValueError) as e:
            print(f"{e}")


if (__name__ == "__main__"):
    plant_datas = [
        ("tomato", 4, 8),
        ("lettuce", 4, 0),
        ("", 50, 10),
        ("lol", 4, 2),
        ("test", 50, 4)
    ]
    print("=== Garden Management System ===\n")
    garden = GardenManager
    garden.add_many_plants(plant_datas)
    garden.water_plants()
    garden.check_plant_health()
    print("Testing error recovery...")
    print(garden.issues)
    print("System recovered and continuing...\n"
          "\nGarden management system test complete!")
