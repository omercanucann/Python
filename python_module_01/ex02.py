class Plant:
    def __init__(self, name, height, age, growth):
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def grow(self):
        self.height = self.height + self.growth
    def age(self):
        self.age = self.age + 1
    def show(self):
        print(f"{self.name}: {self.height:.1f} cm {self.age} days old")


def main():
    grow = 0.8
    plant1 = Plant("Rose", 25.0, 30, grow)
    print("=== Garden Plant Growth ===")
    Plant.show(plant1)
    for i in range(1, 8):
        print(f"== Day {i} ==")
        Plant.grow(plant1)
        Plant.age(plant1)
        Plant.show(plant1)
        if i != 7:
            grow = grow + 0.8
    print(f"Growth this week: {grow:.1f} cm")

if __name__ == "__main__":
    main()