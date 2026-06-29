print("=== Garden Temperature ===")

try:
    x = int(input("Input Data: "))
    print(f"Input Data is '{x}'")
    print(f"Temperature is now {x} C")
except ValueError as e:
    print(f"Caught İnput temperature error: {e}")
print("All tests completed - program didn't crash!")