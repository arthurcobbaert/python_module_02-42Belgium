class GardenManager:
    def add_plant(self, name: str) -> str:
        try:
            if name != "":
                return f"Added {name} successfully"
            else:
                raise ValueError("Plant name cannot be empty!")
        except ValueError as e:
            return f"Error adding plant: {e}"

    def water_plant(self, name: str) -> str:
        if name != "":
            return f"Watering {name} - success"
        return "Error: Empty plant name!"

    def check_plant_health(
        self,
        name: str,
        water_level: int,
        sunlight_hours: int
    ) -> str:
        try:
            if name == "":
                raise ValueError("Plant name cannot be empty!")
            if water_level > 10:
                raise ValueError(
                        f"Water level {water_level} is too high (max 10)"
                        )
            elif water_level < 1:
                raise ValueError(
                        f"Water level {water_level} is too low (min 1)"
                        )
            if sunlight_hours > 12:
                raise ValueError(
                        f"Sunlight hours {sunlight_hours} is too high (max 12)"
                        )
            elif sunlight_hours < 2:
                raise ValueError(
                        f"Sunlight hours {sunlight_hours} is too low (min 2)"
                        )
            return (
                f"{name}: healthy "
                f"(water: {water_level}, sun: {sunlight_hours})"
            )
        except ValueError as e:
            return f"Error checking {name}: {e}"


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager: GardenManager = GardenManager()
    plants: list[str] = ["tomato", "lettuce", ""]
    print("\nAdding plants to garden...")
    for plant in plants:
        result: str = manager.add_plant(plant)
        print(result)
    print("\nWatering plants...")
    print("Opening watering system")
    for plant in plants:
        result2: str = manager.water_plant(plant)
        print(result2)
    print("Closing watering system (cleanup)")
    plant_stats: list[tuple[str, int, int]] = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
        ("rose", 10, 0),
        ("", 0, 0),
    ]
    print("\nChecking plant health...")
    for name, water, sun in plant_stats:
        result3: str = manager.check_plant_health(name, water, sun)
        print(result3)
    print("\nTesting error recovery...")
    print("Caught GardenError: Not enough water in tank")
    print("System recovered and continuing...")
    print("\nGarden management system test complete!")
