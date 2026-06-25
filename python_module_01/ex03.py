class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(f"Created: {self.name}: {round(self.height)} cm, {self.age} days old")

def main():
    Plant1 = Plant("Rose", 25, 30)
    Plant2 = Plant("Oak", 200, 365)
    Plant3 = Plant("Cactus", 5, 90)
    Plant4 = Plant("Sunflower", 80, 45)
    Plant5 = Plant("Fern", 15, 120)

    plants = [Plant1, Plant2, Plant3, Plant4, Plant5]

    print("=== Plant Factory Output ===")
    for i in plants:
        i.show()

if __name__ == "__main__":
    main()