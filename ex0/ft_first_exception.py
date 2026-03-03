def check_temperature(temp_str):
	try:
		temp = int(temp_str)
		if temp > 40:
			print(f"Error: {temp}°C is too hot for plants (max 40°C)")
		elif temp < 0:
			print(f"Error: {temp}°C is too cold for plants (min 0°C)")
		else:
			print(f"Temperature {temp}°C is perfect for plants!")
	except ValueError:
		print(f"Error: '{temp_str}' is not a valid number")
def test_temperature_input():
	print("=== Garden Temperature Checker ==")
	temperatures = [25, "abc", 100, -50]
	for temp in temperatures:
		print(f"\nTesting temperature: {temp}")
		check_temperature(temp)
	print("\nAll testes completed - program didn't crash!")
test_temperature_input()
