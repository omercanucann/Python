class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = 0
        self.age = 0
        self.set_height(height) # değeri direkt atamak yerine kontrol ederek atamak.
        self.set_age(age) # Bu, sınıfın içindeki set_height() metodunu çağırır.
        # bunlar olmazsa kullanıcı -10 gibi saçma bir değer verirse o değer olduğu gibi kaydedilir.

    def grow(self, amount=1):
        if amount >= 0:
            self.height += amount
        else:
            print(f"Error: Growth amount cannot be negative.")

    def set_height(self, height):
        if height >= 0:
            self.height = height
        else:
            print(f"Error: Invalid height for {self._name}. Height cannot be negative.")

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            print(f"Error: Invalid height for {self._name}. Age cannot be negative.")

    def get_height(self):
        return self.height
    
    def get_age(self):
        return self.age
    
    def show(self):
        print(f"Current State: {self.name}: {self.height}, cm {self.age} days old")
 
def main():
    Plant1 = Plant("Rose", 25, 30)
    Plant2 = Plant("Oak", 200, 365)
    Plant3 = Plant("Cactus", 5, 90)
    Plant4 = Plant("Sunflower", 80, 45)
    Plant5 = Plant("Fern", 15, 120)

    plant = [Plant1, Plant2, Plant3, Plant4, Plant5]

    print("=== Garden Security System ===")
    for i in plant:
        i.show()
    print("After 5 Cm Grow")
    for x in plant:
        x.grow(5)
        x.show()

if __name__ == "__main__":
    main()