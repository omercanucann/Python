class PlantError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

def water_plant(plant_name):
    if plant_name != plant_name.capitalize(): # capitalize(), bir metnin ilk harfini büyütüp diğer tüm harfleri küçük yapan string metodudur.
        raise PlantError("Invalid plant name to water: '" + plant_name + "'")
    print("Watering " + plant_name + ": [OK]")

def test_watering_system(plants):
    print("Opening watering system")

    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError: ", e)
        print(".. ending tests and returning to main")
        return
    finally: # hata oluşsa da oluşmasa da her durumda çalışacak kod bloğunu tanımlayan yapıdır.
        print("Closing watering system")

def main():
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])

    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])

    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    main() 