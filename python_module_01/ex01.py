class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
# __init__ Python'da bir **kurucu metot (constructor)**tur.
# Bir sınıftan yeni bir nesne oluşturulduğunda otomatik olarak çalışır ve nesnenin başlangıç değerlerini ayarlamak için kullanılır.
# self, sınıftan oluşturulan nesnenin kendisini temsil eder.
# Basit düşünürsek, bir sınıfın içindeki metotların "hangi nesne üzerinde çalıştığını" bilmesini sağlar.
    def show(self): 
        print("Plant Information")
        print("--------------------")
        print(f"{self.name} : {self.height} cm, {self.age} days old")
        print()
# show bir metot (method) tanımıdır. Metot, sınıfın içinde tanımlanan bir fonksiyondur.
# Burada show() metodu bitkinin bilgilerini ekrana yazdırmak için kullanılıyor.
# show() hangi nesnenin bilgilerini göstereceğini self sayesinde bilir.

# Temel olarak her method bir fonksiyondur, ama her fonksiyon method değildir.
# Method Bir sınıfın içinde tanımlanan fonksiyondur. Fonksiyonlarda self yoktur.
# Methodlarda genellikle ilk parametre self olur:

plant1 = Plant("Tomato", 45, 60)
plant2 = Plant("Rose", 25, 30)
plant3 = Plant("Cactus", 15, 120)

plant1.show() # plant1 nesnesinin içindeki show metodunu çalıştır."
plant2.show()
plant3.show()