def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if (temp < 0):
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return
    elif (temp > 40):
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return (temp)
    return


def test_temperature_input():
    print("=== Garden Temperature Checker ===\n")
    temperatures = [
        "25",
        "abc",
        "100",
        "-50"
    ]
    for temp in temperatures:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
        print("")
    print("All tests completed - program didn't crash!")


if (__name__ == "__main__"):
    test_temperature_input()
