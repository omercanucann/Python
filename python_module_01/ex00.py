def main():
    plant = "Rose"
    height = "25 cm"
    age = "30 days"

    print(f"Plant : {plant}")
    print(f"Height : {height}")
    print(f"Age : {age}")

if __name__ == "__main__":
    main()

# __name__, Python'ın her dosya için otomatik oluşturduğu özel bir değişkendir.
# Bir Python dosyasını doğrudan çalıştırırsan, __name__ değeri "__main__" olur.
# Dosya başka bir Python dosyası tarafından import edilirse, __name__ dosyanın modül adı olur.
# "Eğer bu dosya doğrudan çalıştırılıyorsa main() fonksiyonunu çalıştır; başka bir dosya tarafından import ediliyorsa maini çalıştırma.
#  Sadece fonksiyonlar ve değişkenler yüklenir." 