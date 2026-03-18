def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    try:
        if plant_name == "":
            print("\nTesting empty plant name...")
            raise ValueError("Plant name cannot be empty!")
        else:
            print("\nTesting good values...")
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        if 1 <= water_level <= 10:
            print("\nTesting good values...")
            print(f"Water level {water_level} is OK")
        elif water_level > 10:
            print("\nTesting bad water level...")
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            print("\nTesting bad water level...")
            raise ValueError(f"Water level {water_level} is too low (min 1)")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        if 2 <= sunlight_hours <= 12:
            print("\nTesting good values...")
            print(f"Sunlight hours {sunlight_hours} is OK")
        elif sunlight_hours < 2:
            print("\nTesting bad sunlight hours...")
            raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                    )
        else:
            print("\nTesting bad sunlight hours...")
            raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too high (max 12)"
                    )
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    check_plant_health("tomato", 8, 5)
    check_plant_health("", 19, 5)
    check_plant_health("tomato", 10, 20)
    print("\nAll error raising tests completed!")
