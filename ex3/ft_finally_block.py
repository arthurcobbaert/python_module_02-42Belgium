def water_plants(plant_list: list[any]) -> None:
	print("Opening watering system")
	try:
		for plant in plant_list:
			try:
				plant = plant + ""
				print(f"Watering {plant}")
			except TypeError:
				raise ValueError(f"Cannot water {plant} - invalid plant!")
	except ValueError as e:
		print(f"Error: {e}")
	finally:
		print("Closing watering system (cleanup)")

def test_watering_system() -> None:
	print("=== Garden Watering System ===")
	print("\nTesting normal watering...")
	plants: list[str] = ["tomato", "lettuce", "carrots"]
	water_plants(plants)
	print("Watering completed successfully!")
	print("\nTesting with error...")
	plants2: list[any] = ["tomato", None]
	water_plants(plants2)
	print("\nCleanup always happens, even with errors!")
test_watering_system()
