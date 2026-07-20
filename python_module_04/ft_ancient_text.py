import sys
from typing import IO

def main() -> None: # None, bu fonksiyonun bir değer döndürmediğini belirtir.
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing File ' {filename}'")

    try:
        file: IO[str] = open(filename, "r") # filename adlı dosyayı okuma modunda açar ve dönen metin dosyası nesnesini file değişkenine atar.
        # : → değişkenin tipini belirtir (file değişkeni IO[str] tipindedir).
        # IO Input/Output (Giriş/Çıkış) işlemlerini yapan nesnelerin tipini belirtmek için kullanılan bir type hint'tir.

        print("---")
        print(file.read(), end="") # end="" → print()in en sona eklediği yeni satırı kaldırır.
        print("\n---")

        file.close()
        print(f"File '{filename}' closed.")
    except OSError as error: # OSError, dosya veya işletim sistemiyle ilgili bir hata oluştuğunda Python'ın fırlattığı hata (exception) türüdür.
        print(f"Error opening file '{filename}': {error}")

if __name__ == "__main__":
    main()