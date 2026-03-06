class GardenError(Exception):
	pass

class PlantError(GardenError):
	pass

class WaterError(GardenError):
	pass

def check_plant(status: str, plant: str) -> None:
	if status == "wilting":
		raise PlantError(f"The {plant} plant is wilting!")

def check_tank(level: int) -> None:
	if level < 10:
		raise WaterError("Not enough water in the tank!")
	else:
		print("Water level is OK!")

def test_errors() -> None:
	print("=== Custom Garden Errors Demo ===")
	print("\nTesting PlantError...")
	try:
		check_plant("wilting", "tomato")
	except PlantError as e:
		print(f"Caught PlantError: {e}")
	print("\nTesting WaterError...")
	try:
		check_tank(8)
	except WaterError as e:
		print(f"Caught WaterError: {e}")
	print("\nTesting catching all garden errors...")
	test_cases: list[tuple[str, Any]] = [("tank", 8), ("plant", "wilting")]
	for action, val in test_cases:
		try:
			if action == "plant":
				check_plant(val, "tomato")
			else:
				check_tank(val)
		except GardenError as e:
			print(f"Caught a garden error: {e}")
	print("\nAll custom error types work correctly!")
test_errors()
