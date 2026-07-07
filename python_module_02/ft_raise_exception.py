print("=== Garden Temperature ===")

try:
    x = int(input("Input Data: "))
    print(f"Input Data is '{x}'")
    print(f"Temperature is now {x}°C")
    if x > 40:
        print(f"Caught İnput temperature error: {x}°C is too hot plants (max 40 C)")
    if x < 0:
        print(f"Caught input_temperature error: {x}°C is too cold for plants (min 0°C)")
except ValueError as e:
    print(f"Caught İnput temperature error: {e}")
print("All tests completed - program didn't crash!") 