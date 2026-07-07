class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def check_plant():
    raise PlantError("The Tomata plant is wilting!") # raise, bir istisnayı (exception) bilinçli olarak fırlatıp programın hata durumunu bildirmenizi sağlayan anahtar kelimedir,

def check_water():
    raise WaterError("Not enough water in the tank!")

def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as e:
                print("Caught PlantError:", error)

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as error:
        print("Caught WaterError:", error)

    print("Testing catching all garden errors...")

    try:
        check_plant()
    except GardenError as error:
        print("Caught GardenError:", error)

    try:
        check_water()
    except GardenError as error:
        print("Caught GardenError:", error)

    print("All custom error types work correctly!")


test_custom_errors() 