def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):

    count = 0
    for letter in plant_name:
        count += 1
    try:
        if (count == 0):
            raise ValueError("Error: Plant name cannot be empty!")
        elif (water_level < 1):
            raise ValueError(f"Error: Water level {water_level} is "
                             "too low (min 1)")
        elif (water_level > 10):
            raise ValueError(f"Error: Water level {water_level} is "
                             "too high (max 10)")
        elif (sunlight_hours < 2):
            raise ValueError("Error: Sunlight hours "
                             f"{sunlight_hours} is too low (min 2)")
        elif (sunlight_hours > 12):
            raise ValueError("Error: Sunlight hours "
                             f"{sunlight_hours} is too high (max 12)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"{e}")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n"
          "\nTesting good values...")
    check_plant_health("tomato", 5, 5)
    print("\nTesting empty plant name...")
    check_plant_health("", 5, 5)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 5)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print("\nAll error raising tests completed!")


if (__name__ == "__main__"):
    test_plant_checks()
