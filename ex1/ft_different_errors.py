def garden_operation(error_type: str) -> None:
    if error_type == "ValueError":
        int("abc")
    elif error_type == "ZeroDivisionError":
        25 / 0
    elif error_type == "FileNotFoundError":
        open("test.txt", "r")
    elif error_type == "KeyError":
        plants: dict[str, str] = {"rose": "red flowers"}
        print(plants["sunflower"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    errors: list[str] = [
            "ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError"
        ]
    for error in errors:
        print(f"\nTesting {error}...")
        try:
            garden_operation(error)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e.strerror} '{e.filename}' ")
        except KeyError as e:
            print(f"Caught KeyError: {e}")
    print("\nTesting multiple errors together...")
    try:
        garden_operation(error)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")
