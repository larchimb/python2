def garden_operations() -> None:
    try:
        test = int('abc')
    except ValueError:
        print("\nTesting ValueError...\n"
              "Caught ValueError: invalid literal for int()")
    try:
        test = 78 / 0
    except ZeroDivisionError:
        print("\nTesting ZeroDivisionError...\n"
              "Caught ZeroDivisionError: division by zero")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("\nTesting FileNotFoundError...\n"
              "Caught FileNotFoundError: No such file 'missing.txt'")
    try:
        dictionnary = {"Bob": "test"}
        test = dictionnary["Alice"]
    except KeyError:
        print("\nTest KeyError...\n"
              "Caught KeyError: 'missing\\_plant'")
    try:
        test = int('abc')
        test = 78 / 0
        dictionnary = {"Bob": "test"}
        test = dictionnary["Alice"]
        print(f"{test}")

    except (ZeroDivisionError, ValueError):
        print("\nTesting multiple errors together...\n"
              "Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll error types tested successfully!")


if (__name__ == "__main__"):
    test_error_types()
