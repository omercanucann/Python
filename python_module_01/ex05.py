class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age 
    
    def grow(self, amount):
        self.height += amount
    
    def age_up(self):
        self.age += 1
    def show(self):
        print(f"Created: {self.name}: {round(self.height)} cm, {self.age} days old")

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age) # SuperPython’da üst sınıfın (parent class / base class) metoduna veya özelliklerine erişmek için kullanılır.
        # Flower Sınıfı Plant sınıfından türediği için, bu alt sınıfların içinde Plant’in metodlarını tekrar yazmadan çağırabiliyoruz.
        self.color = color

    def bloom(self):
        print(f"{self.color} is blooming beautifully!")

    def show(self):
        super().show()
        print(f"Color : {self.color}")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter): # trunk_diameter: ağaç gövdesinin çapı
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        print(f"{self.name} is producing shade.")
    
    def show(self):
        super().show()
        print(f"Trunk Diameter : {self.trunk_diameter}")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value=0):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value # nutritional_value: besin değeri
    
    def grow(self, amount=1):
        super().grow(amount)
        self.nutritional_value += 5
    
    def age_up(self):
        super().age_up()
        self.nutritional_value += 3
    
    def show(self):
        super().show()
        print(f"Harvest Season : {self.harvest_season}")
        print(f"Nutritional Value = {self.nutritional_value}")

flower1 = Flower("Rose", 25, 1, "Red")
tree1 = Tree("Oak", 300, 10, 40)
Vegetable1 = Vegetable("Carrot", 15, 0, "Autumn")

flower1.bloom()
flower1.show()

tree1.produce_shade()
tree1.show()

Vegetable1.grow(5)
Vegetable1.age_up()
Vegetable1.show()