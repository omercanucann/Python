class Plant:
    class Statistics: # Bu kısım, Plant sınıfının içinde tanımlanmış iç (nested) bir sınıftır. Görevi, her bitki için istatistikleri tutmaktır
        def __init__(self): 
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

            def grow_called(self):
                self.grow_calls += 1
            
            def age_called(self):
                self.age_calls += 1
            
            def show_called(self):
                self.show_calls += 1
            
            def display(self):
                print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")
        
    def __init__(self, name, height, age_days):
        self.name = name
        self.height = height
        self.age_days = age_days
        self.stats = Plant.Statistics() # Statistics sınıfından bir nesne (object) oluşturuyor ve onu self.stats değişkenine koyuyor.
    
    def grow(self, amount):
        self.height += amount
        self.stats.grow_called() #o bitkinin "grow" (büyüme) metodunun kaç kez çağrıldığını 1 artırır.

    def age(self, days):
        self.age_days += days
        self.stats.age_called()

    def show(self):
        self.stats.show_called()
        print(f"{self.name}: {self.height:.1f} cm {self.age_days} days old")

    @staticmethod # Normal bir metodu kullanmak için önce bir nesne oluşturman gerekir. Ama @staticmethod'te nesne oluşturmana gerek yoktur.
    # Bunu doğrudan sınıf üzerinden çağırırsın Çünkü bu fonksiyon sadece days değerine bakıyor; bitkinin adı, boyu veya yaşı (self) ile ilgilenmiyor.
    # Kısaca: @staticmethod, nesne oluşturmadan kullanılabilen, self kullanmayan sınıf fonksiyonudur.
    def older_than_year(days):
        return (days > 365)
    
    @classmethod # @classmethod, sınıfın kendisini (cls) kullanarak yeni nesneler oluşturmak veya sınıfla ilgili işlemler yapmak için kullanılır.
    def anonymous(cls):
        return(cls("Unknown Plant", 0.0, 0)) # cls, Plant sınıfını temsil eder ve yeni bir Plant nesnesi oluşturur.
    
    def display_stats(self):
        self.stats.display() # o bitkiye ait istatistik nesnesinin display() metodunu çalıştırıp istatistikleri ekrana yazdırır.

class Flower(Plant):
    def __init__(self, name, height, age_days, color):
        super().__init__(name, height, age_days)
        self.color = color
        self.bloomed = False # çiçeğin açıp açmadığını tutan bir değişkendir.
    
    def bloom(self):
        self.bloomed = True
    
    def show(self):
        super.show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f"{self.name} has not bloomed yet")

class Tree(Plant):
    class TreeStatistics(Plant.Statistics): # Plant.Statistics sınıfından miras alan yeni bir sınıf oluşturur.
    # Yani TreeStatistics, Statistics sınıfındaki tüm özelliklere sahip olur (grow, age, show sayaçları) ve bunlara ek olarak ağaçlara özel shade sayacını ekleyebilir.
    # Kısaca: TreeStatistics, Statistics sınıfının geliştirilmiş (kalıtım alan) hâlidir.
        def __init__(self):
            super().__init__() # super().__init__(), üst (miras alınan) sınıfın __init__ metodunu çalıştırır.
            self.shade_calls = 0

        def shade_called(self):
            self.shade_calls += 1
        
        def display(self):
            super().display()
            print(f"{self.shade_calls} shade")
        
    def __init__(self, name, height, age_days):
        super().__init__(name, height, age_days)
        self.trunk_diameter = float(self.trunk_diameter)
        self.stats = Tree.TreeStatistics() # Tree sınıfına ait TreeStatistics nesnesi oluşturur ve stats değişkenine kaydeder.
        # Yani artık bu ağaç, normal istatistiklere (grow, age, show) ek olarak shade istatistiğini de tutabilir.
    
    def produce_shade(self):
        self.stats.shade_called() # Ağacın shade (gölge üretme) sayacını 1 artırır.
        print(f"Tree {self.name} now produces a shade of {self.height:.1f} cm long and {self.trunk_diameter:.1f} cm wide.")
    
    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f} cm")
    
class Seed(Flower):
    def __init__(self, name, height, age_days, color):
        super().__init__(name, height, age_days, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()

def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? ->",
        Plant.older_than_year(30)
    )
    print(
        "Is 400 days more than a year? ->",
        Plant.older_than_year(400)
    )

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()