class WateringError(Exception):
    pass


def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    nb = len(plant_list)
    try:
        for plant in plant_list:
            if (type(plant) is not str):
                raise WateringError(str(plant))
            print(f"Watering {plant}")
            nb -= 1
    except WateringError as e:
        print(f"Error: Cannot water {e} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")
    if (nb == 0):
        print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===\n"
          "\nTesting normal watering...")
    plant_list = [
        "tomato",
        "lettuce",
        "carrots",
    ]
    water_plants(plant_list)
    print("\nTesting with error...")
    plant_list = [
        "tomato",
        15
    ]
    water_plants(plant_list)
    print("\nCleanup always happens, even with errors!")


if (__name__ == "__main__"):
    test_watering_system()
