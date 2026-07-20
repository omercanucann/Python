import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ft_archive_creation.py <filename>")
        return
    
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Error: File not found.")
        return
    
    content = file.read()
    print("---")
    print(content, end="")
    print("---")

    file.close()
    print(f"File '{filename}' closed.")

    print("Transform data:")
    print("---")

    lines = content.split("\n")
    new_content = ""

    for i in range(len(lines)):
        if lines[i] != "":
            new_content += lines[i] + '#'
        if i != len(lines) -1:
            new_content += '#'
    # lines listesindeki her satırı dolaşarak boş olmayan satırların sonuna # ekler ve satırlar arasındaki satır sonlarını 
    # (\n) koruyarak yeni bir metin (new_content) oluşturur.
    
    print(new_content)
    print("---")

    new_filename = input("Enter new file name (or empty): ")

    if new_filename == "":
        print("Not saving data.")
        return
    
    print(f"Saving data to '{new_filename}'")

    new_file = open(new_filename, "w")
    new_file.write(new_content)
    new_file.close()

    print(f"Data saved in file '{new_filename}'.")

if __name__ == "__main__":
    main()